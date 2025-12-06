label nav_menu:
    scene nav_bg
    with fade

    "This is the navigation menu. From here, you can choose where to go next."
    
    menu:
        "Go to the bedroom scene":
            jump scene_1_bedroom
        
        "Return":
            return