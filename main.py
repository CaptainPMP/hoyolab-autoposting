import pyautogui
import time

# Function to move mouse to a specific template location and click
def move_to_template_and_click(template_image, click=True):
    try:
        # Locate the center of the template image on the screen
        location = pyautogui.locateCenterOnScreen(template_image, confidence=0.8)
        
        if location is not None:
            # Move mouse to the center of the template location
            pyautogui.moveTo(location)
            
            # Optionally click on the template location
            if click:
                pyautogui.click()
            
            return True
        else:
            print(f"Template image '{template_image}' not found on the screen.")
            return False
    
    except Exception as e:
        print(f"Error: {e}")
        return False

# Function to type text using pyautogui
def type_text(text):
    pyautogui.typewrite(text, interval=0.1)  # Adjust interval as needed

# Main script
if __name__ == "__main__":
    title_template = 'title_template.png'
    context_template = 'context_template.png'
    interest_image = 'interest.png'
    genshin_image = 'genshin.png'
    category_image = 'category.png'
    discuss_image = 'discuss.png'
    topic_image = 'Topic.png'
    raiden_image = 'Raiden.png'
    publish_image = 'publish.png'
    write = 'write.png'
    post = 'post.png'
    topic2 = 'topic2.png'
    hsr = 'hsr.png'
    acheron = 'acheron.png'
    kafka = 'kafka.png'

    time.sleep(5)
    
    move_to_template_and_click(write)
    time.sleep(1)
    move_to_template_and_click(post)
    time.sleep(1)

    move_to_template_and_click(title_template)
    type_text("In event story, I found out this")
    
    move_to_template_and_click(context_template)
    type_text("I only saw her just like 1 second. I wonder why she has few roles. She has few roles in ayaya forest too...")

    pyautogui.scroll(-1000)

    move_to_template_and_click(interest_image)
    time.sleep(1)
    move_to_template_and_click(genshin_image)
    time.sleep(1)
    move_to_template_and_click(category_image)
    time.sleep(1)
    move_to_template_and_click(discuss_image)
    time.sleep(1)
    move_to_template_and_click(topic_image)
    time.sleep(1)
    type_text("Raiden")
    time.sleep(1)
    move_to_template_and_click(raiden_image)
    time.sleep(1)
    move_to_template_and_click(publish_image)
    pyautogui.scroll(1000)
    time.sleep(1)
    move_to_template_and_click(write)
    time.sleep(1)
    move_to_template_and_click(post)
    time.sleep(1)
    
    move_to_template_and_click(title_template)
    type_text("Recommended team for who has both Acheron and Kafka")
    
    move_to_template_and_click(context_template)
    type_text("Because both are electro and they both nihility, only problem is skills point. for me, Kafka can use normal attack is just fine for me.")

    pyautogui.scroll(-1000)

    move_to_template_and_click(interest_image)
    time.sleep(1)
    move_to_template_and_click(hsr)
    time.sleep(1)
    move_to_template_and_click(category_image)
    time.sleep(1)
    move_to_template_and_click(discuss_image)
    time.sleep(1)
    move_to_template_and_click(topic_image)
    time.sleep(1)
    type_text("ache")
    time.sleep(1)
    move_to_template_and_click(acheron)
    time.sleep(1)
    move_to_template_and_click(topic2)
    time.sleep(1)
    type_text("kafka")
    time.sleep(1)
    move_to_template_and_click(kafka)
    time.sleep(1)
    move_to_template_and_click(publish_image)
