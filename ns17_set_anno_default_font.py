from hiero.core import events, AnnotationText

def set_annotation_font(event): 
    text_annotations = [element for element in event.annotation.elements() if isinstance(element, AnnotationText)] 
    for t in text_annotations: 
        if t.fontFamily() == "Verdana":
            t.setFontFamily("SF Mono")
            t.setFontSize(36)

events.registerInterest("kAnnotationChanged", set_annotation_font)