# This is NOT meant to aid in the relocation of our gnome packages but
# only in the building of software not included in Solaris gnome.

%include machine-header.spec

%if %{which_gnome} == "REPOSITORY"
%define glib_prefix  /usr/local
%define gtk_prefix   /usr/local
%define imlib_prefix /usr/local
%define gnome_prefix /usr/local

%define glib_pkg     glib
%define glib_dev     glib
%define gtk_pkg      gtk+
%define gtk_dev      gtk+-devel
%define imlib_pkg    imlib
%define imlib_dev    imlib-devel
%define gnome_pkg    gnome-libs
%define gnome_dev    gnome-libs-devel

%define gnome_ldflags  -L/usr/local/lib -R/usr/local/lib
%define gnome_cppflags -I/usr/local/include
%endif

# Regarding GNOME, we generally drop repository packages in favor of
# their repository counterparts.  However, we include packages that
# require gtk+ (e.g. vim, freeciv), necessitating these macros:

%if %{which_gnome} == "SOLARIS"
%ifos solaris2.8
%define glib_prefix  /opt/gnome-1.4
%define gtk_prefix   /opt/gnome-1.4
%define imlib_prefix /opt/gnome-1.4
%define gnome_prefix /opt/gnome-1.4

%define glib_pkg     vpkg-SUNWglib
%define glib_dev     vpkg-SUNWglib
%define gtk_pkg      vpkg-SUNWgtk+
%define gtk_dev      vpkg-SUNWgtk+
%define imlib_pkg    vpkg-SUNWimlib
%define imlib_dev    vpkg-SUNWimlib
%define gnome_pkg    vpkg-SUNWglibs
%define gnome_dev    vpkg-SUNWglibs

%define gnome_ldflags  -L/opt/gnome-1.4/lib -R/opt/gnome-1.4/lib
%define gnome_cppflags -I/opt/gnome-1.4/include
%endif

%ifos solaris2.9
%define glib_prefix  /usr/sfw
%define gtk_prefix   /usr/sfw
%define imlib_prefix /usr/sfw
%define gnome_prefix /usr/sfw

%define glib_pkg     vpkg-SUNWGlib
%define glib_dev     vpkg-SUNWGlib
%define gtk_pkg      vpkg-SUNWGtku
%define gtk_dev      vpkg-SUNWGtku
%define imlib_pkg    vpkg-SUNWimlib
%define imlib_dev    vpkg-SUNWimlib
%define gnome_pkg    vpkg-SUNWglibs
%define gnome_dev    vpkg-SUNWglibs

%define gnome_ldflags  -L/usr/sfw/lib -R/usr/sfw/lib
%define gnome_cppflags -I/usr/sfw/include
%endif

%endif

