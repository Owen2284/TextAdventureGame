# Rooms have four fields: name, description, items, and exits

rooms = {
    "room3b" : {
        "name" : "Class 3-B",
        "description" : "",
        "items" : ["ruler", "apple"],
        "exits" : [
            {
                "name" : "class door",
                "destination" : "corridor",
                "item" : "",
                "success" : "You leave the room.",
                "failure" : ""
            },
            {
                "name" : "window",
                "destination" : "freedom",
                "item" : "key",
                "success" : "You try to unlock the window, but you can't get the key into the lock. Instead, you jump through thw window!",
                "failure" : "The window is locked. Of course."
            }
        ]
    },
}