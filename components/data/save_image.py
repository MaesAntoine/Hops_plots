import base64
import os
import ghhops_server as hs

class SaveImage:
    @staticmethod
    def register(hops):
        @hops.component(
            "/save_image",
            name="Save Image",
            nickname="saveimg",
            description="Save a base64 encoded image to a file",
            inputs=[
                hs.HopsString("Base64", "B", "Base64 encoded image string"),
                hs.HopsString("FilePath", "P", "File path to save the image"),
                hs.HopsString("FileName", "N", "File name for the image"),
                hs.HopsBoolean("Save", "S", "Boolean to trigger saving", default=True)
            ],
            outputs=[
                hs.HopsString("Status", "O", "Operation status")
            ]
        )
        def save_image_function(base64_string: str, file_path: str, file_name: str, save: bool = True):
            if not save:
                return "Image not saved (save option set to False)"
            
            try:
                # Ensure the directory exists
                os.makedirs(file_path, exist_ok=True)
                
                # Construct the full file path
                full_path = os.path.join(file_path, file_name)
                
                # Decode the base64 string
                image_data = base64.b64decode(base64_string)
                
                # Write the image data to a file
                with open(full_path, 'wb') as file:
                    file.write(image_data)
                
                return f"Image successfully saved to {full_path}"
            
            except Exception as e:
                return f"Error saving image: {str(e)}"

        return save_image_function