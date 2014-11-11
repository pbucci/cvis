Dependencies
============

Bokeh <http://bokeh.pydata.org/>
Anaconda <https://store.continuum.io/cshop/anaconda/>
ZODB <http://www.zodb.org/>

Notes
=====

There are two layers to this system: the data layer and the display/interaction layer, effectively the frontend and the backend. The frontend uses Bokeh, and the backend is split into three layers : the data layer, the processing layer, and the database. For this version, Bokeh interacts only with the database layer for the backend, since the data will be static. The processing layer produces the data that will appear in the database.

This discretization of the layers is justified by the nature of the data and tasks: we're working with a static set of texts and finite number of interactions that will rely on metadata that can be easily precomputed. Put simply, text processing could take days and not be a big deal, but interactions with the vis tool should be quick, and storage space is not a concern.

Data abstractions
=================

Data processing will build up metadata about a set of texts. Here is a description of the objects built.

Database structure:
