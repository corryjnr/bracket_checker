# GUI program with Tkinter
Python has a lot of GUI frameworks, but Tkinter is the only framework that’s built into the Python standard library.

## using widgets
Widgets are important in Python GUI framework Tkinter. They’re the elements through which users interact with your program.the 
following widget classes were used:
  Label -	A widget used to display text on the screen
  Button -	A button that can contain text and can perform an action when clicked
  Entry -	A text entry widget that allows only a single line of text
  Text -	A text entry widget that allows multiline text entry
  Frame -	A rectangular region used to group related widgets or provide padding between widgets

## Using Events and Event Handlers
When you create a Tkinter application, you must call window.mainloop() to start the event loop. During the event loop, your 
application checks if an event has occurred. If so, then it’ll execute some code in response.
The event loop is provided for you with Tkinter, so you don’t have to write any code that checks for events yourself. 
However, you do have to write the code that will be executed in response to an event. In Tkinter, you write functions 
called event handlers for the events that you use in your application.

# GUI program with wxpython
wxpython is one of the biggest GUI interface tools in python programming. Each of these toolkits will work with Windows,
macOS, and Linux, with PyQt having the additional capability of working on mobile.

## Getting Started With wxPython
The wxPython GUI toolkit is a Python wrapper around a C++ library called wxWidgets. wxPython’s primary difference from other
toolkits is that wxPython uses the actual widgets on the native platform whenever possible. This makes wxPython applications look
native to the operating system that it is running on.
The wxPython downloads page has a section called Extra Files that is worth checking out.

## installing wxpython
You will be using the latest wxPython for this article, which is wxPython 4, also known as the Phoenix release. The wxPython 
3 and wxPython 2 versions are built only for Python 2. When Robin Dunn, the primary maintainer of wxPython, created the wxPython
4 release, he deprecated a lot of aliases and cleaned up a lot of code to make wxPython more Pythonic and easier to maintain.

## Widgets
The wxPython toolkit has more than one hundred widgets to choose from. This allows you to create rich applications, but it can 
also be daunting trying to figure out which widget to use. This is why the wxPython Demo is helpful, as it has a search filter
that you can use to help you find the widgets that might apply.

# GUI program with kivy
## kivy framework
Kivy was first released in early 2011.  It supports multitouch events in addition to regular keyboard and mouse inputs. Kivy even 
supports GPU acceleration of itsgraphics. The project uses the MIT license, so you can use this library for free and 
commercial software.
When you create an application with Kivy, you’re creating a Natural User Interface or NUI. The idea behind a Natural User
Interface is that the user can easily learn how to use your software with little to no instruction.
Kivy does not attempt to use native controls or widgets. All of its widgets are custom-drawn. This means that Kivy applications
will look the same across all platforms. However, it also means that your app’s look and feel will differ from your user’s native
applications. This could be a benefit or a drawback, depending on your audience.

##installing kivy
Kivy has many dependencies, so it’s recommended that you install it into a Python virtual environment. You can use either Python’s built-in venv library or the virtualenv package. If you’ve never used a Python virtual environment before, then check out Python Virtual Environments: A Primer.
To use your virtual environment, you need to activate it. On Mac and Linux.
The command for Windows is similar, but the location of the activate script is inside of the Scripts folder instead of bin.
Now that you have an activated Python virtual environment, you can run pip to install Kivy. On Linux and Mac.
If you run into any issues installing Kivy on your platform, then see the Kivy download page for additional instructions.

## kivy widgets
All graphical user interface toolkits come with a set of widgets. Some common widgets that you may have used include buttons,
combo boxes, and tabs. Kivy has many widgets built into its framework.

## Using the KV Language
Kivy also provides a design language called KV that you can use with your Kivy applications. The KV language lets you separate
your interface design from the application’s logic. This follows the separation of concerns principle and is part of the
Model-View-Controller architectural pattern.
  
  