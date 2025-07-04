import argparse
import numpy as np
import ast # For safely evaluating string literals

def numpy_array_type(arg_string):
    """
    Custom type function for argparse to convert a string
    representation of a list into a numpy array.
    """
    try:
        # Safely evaluate the string as a Python literal (list, tuple, etc.)
        list_representation = ast.literal_eval(arg_string)

        # Convert the Python list/tuple to a NumPy array
        np_array = np.array(list_representation)
        return np_array
    except (ValueError, SyntaxError) as e:
        # Raise an ArgumentTypeError for argparse to handle
        raise argparse.ArgumentTypeError(
            f"Invalid numpy array format: '{arg_string}' "
            f"Expected a string representation of a list/tuple (e.g., '[[1,2],[3,4]]'). Error: {e}"
        )
    except Exception as e:
        raise argparse.ArgumentTypeError(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process a NumPy array passed as a command-line argument."
    )

    # Add an argument named '--data_array' that uses our custom type converter
    parser.add_argument(
        '--data_array',
        type=numpy_array_type,
        required=True, # Make it a required argument
        help='A NumPy array passed as a string representation of a Python list, e.g., "[[1, 2], [3, 4]]"'
    )

    args = parser.parse_args()

    print("Received NumPy Array:")
    print(args.data_array)
    print(f"Type: {type(args.data_array)}")
    print(f"Shape: {args.data_array.shape}")
    print(f"Dtype: {args.data_array.dtype}")

    # You can now use args.data_array as a normal NumPy array
    print("\nPerforming a simple operation (e.g., mean):")
    print(f"Mean of array: {np.mean(args.data_array)}")