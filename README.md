# Reverse Phone Lookup

There are a number of sources for different tidbits of information by phone number, I'm trying to
consolidate those. At this point (although check, because I often forget to update the README) there
aren't a lot of sources and some of them are only useful for an extremely specific set of numbers
(such as the University of Washington directory). All sources are plugins, and I'd encourage you to
write and commit your own.

# Dependencies
The main program has no dependencies other than python and the modules that come with it. Most
plugins have one or two dependencies.

# Plugins
The following plugins are available currently (feel free to write your own!):

## OpenCNAM
Uses the [OpenCNAM](https://www.opencnam.com/) API to try to find the caller ID of the number. Not
terribly reliable, but free :)

## UW Directory
Uses the University of Washington [Student, Faculty and Staff directory](https://www.washington.edu/home/peopledir/),
which includes student cellphone numbers, to try to find a name and email associated with the
number. The UW directory may have additional information, such as additional phone numbers, field of
study for students or department for faculty/staff which is not displayed at this time, although I
should add it one day.

# Contributing
Please contribute! There are lots of fun data sources that I haven't come up with. The plugin
structure should be pretty self explanatory, both the OpenCNAM and UW Directory plugins are under
30 lines and should be easy to read. Eventually I'll write up official API docs.

# TODO:
 - [ ] Allow a plugin to indicate if it's ready for use (eg if it's dependencies are installed).
 This may also come in handy when there is configuration needed for plugins.
 - [ ] Configuration. Some plugins may need configuration (such as private API keys), and I'd like
 to add a standard way of doing that
 - [ ] More data sources. Always need more data.
