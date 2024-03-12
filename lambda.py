import json
import ast
import sagemaker
import base64
import boto3
from sagemaker.serializers import IdentitySerializer

s3 = boto3.client('s3')
def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = event["s3_key"]  # The S3 object key
    bucket = event["s3_bucket"]  # The S3 bucket name

    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, key, "/tmp/image.png")

    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())
        event["image_data"] = image_data
    # Pass the data back to the Step Function
    print("Event:", event.keys())
    print( {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }})
    return event

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-08-23-19-59-51-868"  # Replace with your actual endpoint

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])  # Decode the base64-encoded image data

    # Instantiate a Predictor
    try:
        predictor = sagemaker.predictor.Predictor(
            ENDPOINT,
            sagemaker_session=sagemaker.Session(),
        )
            # For this model, the IdentitySerializer needs to be "image/png"
        predictor.serializer = IdentitySerializer("image/png")
    
        # Make a prediction
        inferences = predictor.predict(image)  # Use the decoded image data
    
        # We return the data back to the Step Function    
        event["inferences"] = inferences.decode('utf-8')
        print({
            'statusCode': 200,
            'body': json.dumps(event),
            'event': event
        })
        return event
    except Exception as e:
        print(e)

THRESHOLD = 0.93

def lambda_handler(event, context):
    # Grab the inferences from the event
    inferences = event.get("inferences", [])  # TODO: fill in
    list_inferences = ast.literal_eval(inferences)
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(inference >= THRESHOLD for inference in list_inferences)# TODO: fill in

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
