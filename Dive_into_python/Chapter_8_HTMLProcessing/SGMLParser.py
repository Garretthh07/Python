#!usr/bin/python
# Filename: SGMLParser.py

def finish_starttag(self, tag, attrs):
    try:
        method = getattr(self, 'start_' + tag)
    except AttributeError:
        try:
            method = getattr(self, 'do_' + tag)
        except AttributeError:
            self.unknown_starttag(tag, attrs)
            return -1
        else:
            self.handle_starttag(tag, method, attrs)
            return 0
        else:
            self.stack.append(tag)
            self.handle_starttag(tag, method, attrs)
            return 1

def handle_starttag(self, tag, method, attrs):
    method(attrs)

