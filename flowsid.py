import graphics, cursor, text

graphics.init()
text.init()

info = text.render('FlowSID v0.0.1')
info.rect.topleft = (1, 1)
graphics.toplayer.add(info)

cursor = cursor.Cursor() 

def handle_event(event):
    pass

graphics.render_loop(handle_event)
