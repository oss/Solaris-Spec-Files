Summary: glib2
Name: glib2
Version: 2.2.2
Release: 3
Copyright: GPL
Group: Applications/Editors
Source: glib-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: pkgconfig

%description
glib2

%package devel
Summary: %{name} include files, etc.
Requires: %{name} %{buildrequires}
Group: Development
%description devel
%{name} include files, etc.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation


%prep
%setup -q -n glib-%{version}

%build
CC="gcc" ./configure --prefix=/usr/local --disable-nls --disable-rebuilds


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/glib-genmarshal
/usr/local/bin/glib-gettextize
/usr/local/bin/glib-mkenums
/usr/local/bin/gobject-query
/usr/local/lib/glib-2.0
/usr/local/lib/glib-2.0/include
/usr/local/lib/glib-2.0/include/glibconfig.h
/usr/local/lib/libglib-2.0.so*
/usr/local/lib/libgmodule-2.0.so*
/usr/local/lib/libgobject-2.0.so*
/usr/local/lib/libgthread-2.0.so*
/usr/local/man/man1/glib-genmarshal.1
/usr/local/man/man1/glib-mkenums.1

%files devel
%defattr(-,root,other)
/usr/local/share/aclocal/glib-2.0.m4
/usr/local/share/aclocal/glib-gettext.m4
/usr/local/share/glib-2.0/gettext/po/Makefile.in.in
/usr/local/lib/pkgconfig/glib-2.0.pc
/usr/local/lib/pkgconfig/gmodule-2.0.pc
/usr/local/lib/pkgconfig/gobject-2.0.pc
/usr/local/lib/pkgconfig/gthread-2.0.pc
/usr/local/include/*
#/usr/local/include/glib-2.0/glib-object.h
#/usr/local/include/glib-2.0/glib.h
#/usr/local/include/glib-2.0/glib/galloca.h
#/usr/local/include/glib-2.0/glib/garray.h
#/usr/local/include/glib-2.0/glib/gasyncqueue.h
#/usr/local/include/glib-2.0/glib/gbacktrace.h
#/usr/local/include/glib-2.0/glib/gcache.h
#/usr/local/include/glib-2.0/glib/gcompletion.h
#/usr/local/include/glib-2.0/glib/gconvert.h
#/usr/local/include/glib-2.0/glib/gdataset.h
#/usr/local/include/glib-2.0/glib/gdate.h
#/usr/local/include/glib-2.0/glib/gdir.h
#/usr/local/include/glib-2.0/glib/gerror.h
#/usr/local/include/glib-2.0/glib/gfileutils.h
#/usr/local/include/glib-2.0/glib/ghash.h
#/usr/local/include/glib-2.0/glib/ghook.h
#/usr/local/include/glib-2.0/glib/giochannel.h
#/usr/local/include/glib-2.0/glib/glist.h
#/usr/local/include/glib-2.0/glib/gmacros.h
#/usr/local/include/glib-2.0/glib/gmain.h
#/usr/local/include/glib-2.0/glib/gmarkup.h
#/usr/local/include/glib-2.0/glib/gmem.h
#/usr/local/include/glib-2.0/glib/gmessages.h
#/usr/local/include/glib-2.0/glib/gnode.h
#/usr/local/include/glib-2.0/glib/gpattern.h
#/usr/local/include/glib-2.0/glib/gprimes.h
#/usr/local/include/glib-2.0/glib/gprintf.h
#/usr/local/include/glib-2.0/glib/gqsort.h
#/usr/local/include/glib-2.0/glib/gquark.h
#/usr/local/include/glib-2.0/glib/gqueue.h
#/usr/local/include/glib-2.0/glib/grand.h
#/usr/local/include/glib-2.0/glib/grel.h
#/usr/local/include/glib-2.0/glib/gscanner.h
#/usr/local/include/glib-2.0/glib/gshell.h
#/usr/local/include/glib-2.0/glib/gslist.h
#/usr/local/include/glib-2.0/glib/gspawn.h
#/usr/local/include/glib-2.0/glib/gstrfuncs.h
#/usr/local/include/glib-2.0/glib/gstring.h
#/usr/local/include/glib-2.0/glib/gthread.h
#/usr/local/include/glib-2.0/glib/gthreadpool.h
#/usr/local/include/glib-2.0/glib/gtimer.h
#/usr/local/include/glib-2.0/glib/gtree.h
#/usr/local/include/glib-2.0/glib/gtypes.h
#/usr/local/include/glib-2.0/glib/gunicode.h
#/usr/local/include/glib-2.0/glib/gutils.h
#/usr/local/include/glib-2.0/glib/gwin32.h
#/usr/local/include/glib-2.0/gmodule.h
#/usr/local/include/glib-2.0/gobject/gboxed.h
#/usr/local/include/glib-2.0/gobject/gclosure.h
#/usr/local/include/glib-2.0/gobject/genums.h
#/usr/local/include/glib-2.0/gobject/gmarshal.h
#/usr/local/include/glib-2.0/gobject/gobject.h
#/usr/local/include/glib-2.0/gobject/gobjectnotifyqueue.c
#/usr/local/include/glib-2.0/gobject/gparam.h
#/usr/local/include/glib-2.0/gobject/gparamspecs.h
#/usr/local/include/glib-2.0/gobject/gsignal.h
#/usr/local/include/glib-2.0/gobject/gsourceclosure.h
#/usr/local/include/glib-2.0/gobject/gtype.h
#/usr/local/include/glib-2.0/gobject/gtypemodule.h
#/usr/local/include/glib-2.0/gobject/gtypeplugin.h
#/usr/local/include/glib-2.0/gobject/gvalue.h
#/usr/local/include/glib-2.0/gobject/gvaluearray.h
#/usr/local/include/glib-2.0/gobject/gvaluecollector.h
#/usr/local/include/glib-2.0/gobject/gvaluetypes.h

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/html/glib/glib-Arrays.html
/usr/local/share/gtk-doc/html/glib/glib-Asynchronous-Queues.html
/usr/local/share/gtk-doc/html/glib/glib-Automatic-String-Completion.html
/usr/local/share/gtk-doc/html/glib/glib-Balanced-Binary-Trees.html
/usr/local/share/gtk-doc/html/glib/glib-Basic-Types.html
/usr/local/share/gtk-doc/html/glib/glib-Byte-Arrays.html
/usr/local/share/gtk-doc/html/glib/glib-Byte-Order-Macros.html
/usr/local/share/gtk-doc/html/glib/glib-Caches.html
/usr/local/share/gtk-doc/html/glib/glib-Character-Set-Conversion.html
/usr/local/share/gtk-doc/html/glib/glib-Datasets.html
/usr/local/share/gtk-doc/html/glib/glib-Date-and-Time-Functions.html
/usr/local/share/gtk-doc/html/glib/glib-Double-ended-Queues.html
/usr/local/share/gtk-doc/html/glib/glib-Doubly-Linked-Lists.html
/usr/local/share/gtk-doc/html/glib/glib-Dynamic-Loading-of-Modules.html
/usr/local/share/gtk-doc/html/glib/glib-Error-Reporting.html
/usr/local/share/gtk-doc/html/glib/glib-File-Utilities.html
/usr/local/share/gtk-doc/html/glib/glib-Glob-style-pattern-matching.html
/usr/local/share/gtk-doc/html/glib/glib-Hash-Tables.html
/usr/local/share/gtk-doc/html/glib/glib-Hook-Functions.html
/usr/local/share/gtk-doc/html/glib/glib-IO-Channels.html
/usr/local/share/gtk-doc/html/glib/glib-Keyed-Data-Lists.html
/usr/local/share/gtk-doc/html/glib/glib-Lexical-Scanner.html
/usr/local/share/gtk-doc/html/glib/glib-Limits-of-Basic-Types.html
/usr/local/share/gtk-doc/html/glib/glib-Memory-Allocation.html
/usr/local/share/gtk-doc/html/glib/glib-Memory-Allocators.html
/usr/local/share/gtk-doc/html/glib/glib-Memory-Chunks.html
/usr/local/share/gtk-doc/html/glib/glib-Message-Logging.html
/usr/local/share/gtk-doc/html/glib/glib-Miscellaneous-Macros.html
/usr/local/share/gtk-doc/html/glib/glib-Miscellaneous-Utility-Functions.html
/usr/local/share/gtk-doc/html/glib/glib-N-ary-Trees.html
/usr/local/share/gtk-doc/html/glib/glib-Numerical-Definitions.html
/usr/local/share/gtk-doc/html/glib/glib-Pointer-Arrays.html
/usr/local/share/gtk-doc/html/glib/glib-Quarks.html
/usr/local/share/gtk-doc/html/glib/glib-Random-Numbers.html
/usr/local/share/gtk-doc/html/glib/glib-Relations-and-Tuples.html
/usr/local/share/gtk-doc/html/glib/glib-Shell-related-Utilities.html
/usr/local/share/gtk-doc/html/glib/glib-Simple-XML-Subset-Parser.html
/usr/local/share/gtk-doc/html/glib/glib-Singly-Linked-Lists.html
/usr/local/share/gtk-doc/html/glib/glib-Spawning-Processes.html
/usr/local/share/gtk-doc/html/glib/glib-Standard-Macros.html
/usr/local/share/gtk-doc/html/glib/glib-String-Chunks.html
/usr/local/share/gtk-doc/html/glib/glib-String-Utility-Functions.html
/usr/local/share/gtk-doc/html/glib/glib-Strings.html
/usr/local/share/gtk-doc/html/glib/glib-The-Main-Event-Loop.html
/usr/local/share/gtk-doc/html/glib/glib-Thread-Pools.html
/usr/local/share/gtk-doc/html/glib/glib-Threads.html
/usr/local/share/gtk-doc/html/glib/glib-Timers.html
/usr/local/share/gtk-doc/html/glib/glib-Trash-Stacks.html
/usr/local/share/gtk-doc/html/glib/glib-Type-Conversion-Macros.html
/usr/local/share/gtk-doc/html/glib/glib-Unicode-Manipulation.html
/usr/local/share/gtk-doc/html/glib/glib-Warnings-and-Assertions.html
/usr/local/share/gtk-doc/html/glib/glib-Windows-Compatability-Functions.html
/usr/local/share/gtk-doc/html/glib/glib-building.html
/usr/local/share/gtk-doc/html/glib/glib-changes.html
/usr/local/share/gtk-doc/html/glib/glib-compiling.html
/usr/local/share/gtk-doc/html/glib/glib-core.html
/usr/local/share/gtk-doc/html/glib/glib-data-types.html
/usr/local/share/gtk-doc/html/glib/glib-fundamentals.html
/usr/local/share/gtk-doc/html/glib/glib-resources.html
/usr/local/share/gtk-doc/html/glib/glib-running.html
/usr/local/share/gtk-doc/html/glib/glib-utilities.html
/usr/local/share/gtk-doc/html/glib/glib.devhelp
/usr/local/share/gtk-doc/html/glib/glib.html
/usr/local/share/gtk-doc/html/glib/home.png
/usr/local/share/gtk-doc/html/glib/index.html
/usr/local/share/gtk-doc/html/glib/index.sgml
/usr/local/share/gtk-doc/html/glib/left.png
/usr/local/share/gtk-doc/html/glib/mainloop-states.gif
/usr/local/share/gtk-doc/html/glib/right.png
/usr/local/share/gtk-doc/html/glib/up.png
/usr/local/share/gtk-doc/html/gobject/gobject-Boxed-Types.html
/usr/local/share/gtk-doc/html/gobject/gobject-Closures.html
/usr/local/share/gtk-doc/html/gobject/gobject-Enumeration-and-Flag-Types.html
/usr/local/share/gtk-doc/html/gobject/gobject-GParamSpec.html
/usr/local/share/gtk-doc/html/gobject/gobject-GType.html
/usr/local/share/gtk-doc/html/gobject/gobject-GTypeModule.html
/usr/local/share/gtk-doc/html/gobject/gobject-GTypePlugin.html
/usr/local/share/gtk-doc/html/gobject/gobject-Generic-values.html
/usr/local/share/gtk-doc/html/gobject/gobject-Signals.html
/usr/local/share/gtk-doc/html/gobject/gobject-Standard-Parameter-and-Value-Types.html
/usr/local/share/gtk-doc/html/gobject/gobject-The-Base-Object-Type.html
/usr/local/share/gtk-doc/html/gobject/gobject-Value-arrays.html
/usr/local/share/gtk-doc/html/gobject/gobject-Varargs-Value-Collection.html
/usr/local/share/gtk-doc/html/gobject/gobject.devhelp
/usr/local/share/gtk-doc/html/gobject/home.png
/usr/local/share/gtk-doc/html/gobject/index.html
/usr/local/share/gtk-doc/html/gobject/index.sgml
/usr/local/share/gtk-doc/html/gobject/left.png
/usr/local/share/gtk-doc/html/gobject/pr01.html
/usr/local/share/gtk-doc/html/gobject/right.png
/usr/local/share/gtk-doc/html/gobject/rn01.html
/usr/local/share/gtk-doc/html/gobject/up.png




