Summary: gtk+
Name: gtk2
Version: 2.2.1
Release: 3
Copyright: GPL
Group: Applications/Editors
Source: gtk+-2.2.1.tar.bz2
Source1: redhat-artwork-0.68-1.src.rpm
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: pango glib2 atk
BuildRequires: pango-devel glib2-devel atk-devel pkgconfig autoconf >= 2.57

%description
gtk

%package devel
Summary: %{name} include files, etc.
Requires: %{name}
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
%setup -q -n gtk+-%{version}

%build
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
LDFLAGS="-R/usr/sfw/lib -L/usr/sfw/lib"
PATH="/usr/local/bin:/usr/sfw/bin:$PATH"
CPPFLAGS="-I/usr/sfw/include"
export LD_LIBRARY_PATH PATH CPPFLAGS LDFLAGS
CC="gcc" ./configure --prefix=/usr/local --disable-nls --disable-rebuilds
make

#This is not the best way to do this. Sorry!
#make install DESTDIR=$RPM_BUILD_ROOT
#PKG_CONFIG_PATH="$RPM_BUILD_ROOT/usr/local/lib/pkgconfig/"
#CPPFLAGS="-I$RPM_BUILD_ROOT/usr/local/include/gtk-2.0:$CPPFLAGS"
#echo $CPPFLAGS
#export PKG_CONFIG_PATH CPPFLAGS

# redhat theme
#BASE=`pwd`
#rpm2cpio %{_sourcedir}/redhat-artwork-0.68-1.src.rpm | cpio -id --
#gunzip redhat-artwork-0.68.tar.gz
#tar xvf redhat-artwork-0.68.tar
#cd redhat-artwork-0.68

#shamelessly stolen from Gentoo
#removes check for gtk1.2 and qt
#        rm configure
#        mv configure.in configure.in.old
#        sed -e  "s|dnl KDE_USE_QT||" \
#                -e "s|KDE_||g" \
#                -e "s|AC_PATH_KDE||" \
#                -e "s|art/kde/Makefile||" \
#                -e "s|art/kde/kwin/Makefile||" \
#                -e "s|art/kde/kwin/Bluecurve/Makefile||" \
#                        configure.in.old > configure.in
                                                                                       
#        mv art/Makefile.am art/Makefile.am.old
#        sed -e  "s|kde||" \
#                -e      "s|qt||" \
#                        art/Makefile.am.old > art/Makefile.am
                                                                                       
#        mv art/Makefile.in art/Makefile.in.old
#        sed -e  "s|kde||" \
#                -e  "s|qt||" \
#                        art/Makefile.in.old > art/Makefile.in
                                                                                
#        mv configure.in configure.in.old
#        sed -e  "s|AM_PATH_GTK(1.2.9, ,||" \
#                -e  "s|AC_MSG_ERROR(.*GTK+-1.*||" \
#                -e  "s|AC_CHECK_LIB(gtk, gtk_style_set_prop_experimental, :,||" \
#                -e  "s|AC_MSG_ERROR(.*gtk_style.*||" \
#                -e  "s|             \$GTK_LIBS)||" \
#                -e  "s|AM_PATH_GDK_PIXBUF||" \
#                -e  "s|art/gtk/Bluecurve1/Makefile||" \
#                -e  "s|art/gtk/Bluecurve1/gtk/Makefile||" \
#        configure.in.old > configure.in
#        mv art/gtk/Makefile.am art/gtk/Makefile.am.old
#        sed -e  "s|Bluecurve1||" \
#        art/gtk/Makefile.am.old > art/gtk/Makefile.am
#	autoconf
#	automake

#./configure
#cd art/gtk/Bluecurve
#make
#cd ..
#mv Bluecurve $BASE

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/
touch $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/gdk-pixbuf.loaders
touch $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/gtk.immodules
make install DESTDIR=$RPM_BUILD_ROOT
#cd redhat-artwork-0.68/art/gtk/Bluecurve
#make install DESTDIR=$RPM_BUILD_ROOT
#mv $RPM_BUILD_ROOT/usr/local/share/themes/Default $RPM_BUILD_ROOT/usr/local/share/themes/Default-gtk
#ln -sf Bluecurve $RPM_BUILD_ROOT/usr/local/share/themes/Default

%post
echo Running gdk-pixbuf-query-loaders...
/usr/local/bin/gdk-pixbuf-query-loaders > /usr/local/etc/gtk-2.0/gdk-pixbuf.loaders
echo Running gtk-query-immodules-2.0...
/usr/local/bin/gtk-query-immodules-2.0 > /usr/local/etc/gtk-2.0/gtk.immodules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/etc/gtk-2.0/gdk-pixbuf.loaders
/usr/local/etc/gtk-2.0/gtk.immodules
/usr/local/bin/gdk-pixbuf-csource
/usr/local/bin/gdk-pixbuf-query-loaders
/usr/local/bin/gtk-demo
/usr/local/bin/gtk-query-immodules-2.0
/usr/local/lib/gtk-2.0
/usr/local/lib/gtk-2.0/2.2.0
/usr/local/lib/gtk-2.0/2.2.0/immodules
/usr/local/lib/gtk-2.0/2.2.0/immodules/im*.so
/usr/local/lib/gtk-2.0/2.2.0/loaders
/usr/local/lib/gtk-2.0/2.2.0/loaders/libpixbufloader-*.so
#/usr/local/lib/gtk-2.0/2.2.0/engines/libbluecurve.so
/usr/local/lib/gtk-2.0/include
/usr/local/lib/gtk-2.0/include/gdkconfig.h
/usr/local/lib/libgdk-x11-2.0.so
/usr/local/lib/libgdk-x11-2.0.so.0
/usr/local/lib/libgdk-x11-2.0.so.0.200.1
/usr/local/lib/libgdk_pixbuf-2.0.so
/usr/local/lib/libgdk_pixbuf-2.0.so.0
/usr/local/lib/libgdk_pixbuf-2.0.so.0.200.1
/usr/local/lib/libgdk_pixbuf_xlib-2.0.so
/usr/local/lib/libgdk_pixbuf_xlib-2.0.so.0
/usr/local/lib/libgdk_pixbuf_xlib-2.0.so.0.200.1
/usr/local/lib/libgtk-x11-2.0.so
/usr/local/lib/libgtk-x11-2.0.so.0
/usr/local/lib/libgtk-x11-2.0.so.0.200.1
/usr/local/lib/pkgconfig/gdk-2.0.pc
/usr/local/lib/pkgconfig/gdk-pixbuf-2.0.pc
/usr/local/lib/pkgconfig/gdk-pixbuf-xlib-2.0.pc
/usr/local/lib/pkgconfig/gdk-x11-2.0.pc
/usr/local/lib/pkgconfig/gtk+-2.0.pc
/usr/local/lib/pkgconfig/gtk+-x11-2.0.pc
/usr/local/man/man1/gdk-pixbuf-csource.1
/usr/local/share/themes/Default
/usr/local/share/themes/Emacs

%files devel
%defattr(-,root,other)
/usr/local/include/gtk-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlib.h
/usr/local/include/gtk-2.0/gdk-pixbuf-xlib/gdk-pixbuf-xlibrgb.h
/usr/local/include/gtk-2.0/gdk-pixbuf/gdk-pixbuf-animation.h
/usr/local/include/gtk-2.0/gdk-pixbuf/gdk-pixbuf-enum-types.h
/usr/local/include/gtk-2.0/gdk-pixbuf/gdk-pixbuf-features.h
/usr/local/include/gtk-2.0/gdk-pixbuf/gdk-pixbuf-io.h
/usr/local/include/gtk-2.0/gdk-pixbuf/gdk-pixbuf-loader.h
/usr/local/include/gtk-2.0/gdk-pixbuf/gdk-pixbuf-marshal.h
/usr/local/include/gtk-2.0/gdk-pixbuf/gdk-pixbuf.h
/usr/local/include/gtk-2.0/gdk-pixbuf/gdk-pixdata.h
/usr/local/include/gtk-2.0/gdk/gdk.h
/usr/local/include/gtk-2.0/gdk/gdkcolor.h
/usr/local/include/gtk-2.0/gdk/gdkcursor.h
/usr/local/include/gtk-2.0/gdk/gdkdisplay.h
/usr/local/include/gtk-2.0/gdk/gdkdisplaymanager.h
/usr/local/include/gtk-2.0/gdk/gdkdnd.h
/usr/local/include/gtk-2.0/gdk/gdkdrawable.h
/usr/local/include/gtk-2.0/gdk/gdkenumtypes.h
/usr/local/include/gtk-2.0/gdk/gdkevents.h
/usr/local/include/gtk-2.0/gdk/gdkfont.h
/usr/local/include/gtk-2.0/gdk/gdkgc.h
/usr/local/include/gtk-2.0/gdk/gdki18n.h
/usr/local/include/gtk-2.0/gdk/gdkimage.h
/usr/local/include/gtk-2.0/gdk/gdkinput.h
/usr/local/include/gtk-2.0/gdk/gdkkeys.h
/usr/local/include/gtk-2.0/gdk/gdkkeysyms.h
/usr/local/include/gtk-2.0/gdk/gdkpango.h
/usr/local/include/gtk-2.0/gdk/gdkpixbuf.h
/usr/local/include/gtk-2.0/gdk/gdkpixmap.h
/usr/local/include/gtk-2.0/gdk/gdkprivate.h
/usr/local/include/gtk-2.0/gdk/gdkproperty.h
/usr/local/include/gtk-2.0/gdk/gdkregion.h
/usr/local/include/gtk-2.0/gdk/gdkrgb.h
/usr/local/include/gtk-2.0/gdk/gdkscreen.h
/usr/local/include/gtk-2.0/gdk/gdkselection.h
/usr/local/include/gtk-2.0/gdk/gdktypes.h
/usr/local/include/gtk-2.0/gdk/gdkvisual.h
/usr/local/include/gtk-2.0/gdk/gdkwindow.h
/usr/local/include/gtk-2.0/gdk/gdkx.h
/usr/local/include/gtk-2.0/gtk/gtk.h
/usr/local/include/gtk-2.0/gtk/gtkaccelgroup.h
/usr/local/include/gtk-2.0/gtk/gtkaccellabel.h
/usr/local/include/gtk-2.0/gtk/gtkaccelmap.h
/usr/local/include/gtk-2.0/gtk/gtkaccessible.h
/usr/local/include/gtk-2.0/gtk/gtkadjustment.h
/usr/local/include/gtk-2.0/gtk/gtkalignment.h
/usr/local/include/gtk-2.0/gtk/gtkarrow.h
/usr/local/include/gtk-2.0/gtk/gtkaspectframe.h
/usr/local/include/gtk-2.0/gtk/gtkbbox.h
/usr/local/include/gtk-2.0/gtk/gtkbin.h
/usr/local/include/gtk-2.0/gtk/gtkbindings.h
/usr/local/include/gtk-2.0/gtk/gtkbox.h
/usr/local/include/gtk-2.0/gtk/gtkbutton.h
/usr/local/include/gtk-2.0/gtk/gtkcalendar.h
/usr/local/include/gtk-2.0/gtk/gtkcelleditable.h
/usr/local/include/gtk-2.0/gtk/gtkcellrenderer.h
/usr/local/include/gtk-2.0/gtk/gtkcellrendererpixbuf.h
/usr/local/include/gtk-2.0/gtk/gtkcellrenderertext.h
/usr/local/include/gtk-2.0/gtk/gtkcellrenderertoggle.h
/usr/local/include/gtk-2.0/gtk/gtkcheckbutton.h
/usr/local/include/gtk-2.0/gtk/gtkcheckmenuitem.h
/usr/local/include/gtk-2.0/gtk/gtkclipboard.h
/usr/local/include/gtk-2.0/gtk/gtkclist.h
/usr/local/include/gtk-2.0/gtk/gtkcolorsel.h
/usr/local/include/gtk-2.0/gtk/gtkcolorseldialog.h
/usr/local/include/gtk-2.0/gtk/gtkcombo.h
/usr/local/include/gtk-2.0/gtk/gtkcontainer.h
/usr/local/include/gtk-2.0/gtk/gtkctree.h
/usr/local/include/gtk-2.0/gtk/gtkcurve.h
/usr/local/include/gtk-2.0/gtk/gtkdebug.h
/usr/local/include/gtk-2.0/gtk/gtkdialog.h
/usr/local/include/gtk-2.0/gtk/gtkdnd.h
/usr/local/include/gtk-2.0/gtk/gtkdrawingarea.h
/usr/local/include/gtk-2.0/gtk/gtkeditable.h
/usr/local/include/gtk-2.0/gtk/gtkentry.h
/usr/local/include/gtk-2.0/gtk/gtkenums.h
/usr/local/include/gtk-2.0/gtk/gtkeventbox.h
/usr/local/include/gtk-2.0/gtk/gtkfilesel.h
/usr/local/include/gtk-2.0/gtk/gtkfixed.h
/usr/local/include/gtk-2.0/gtk/gtkfontsel.h
/usr/local/include/gtk-2.0/gtk/gtkframe.h
/usr/local/include/gtk-2.0/gtk/gtkgamma.h
/usr/local/include/gtk-2.0/gtk/gtkgc.h
/usr/local/include/gtk-2.0/gtk/gtkhandlebox.h
/usr/local/include/gtk-2.0/gtk/gtkhbbox.h
/usr/local/include/gtk-2.0/gtk/gtkhbox.h
/usr/local/include/gtk-2.0/gtk/gtkhpaned.h
/usr/local/include/gtk-2.0/gtk/gtkhruler.h
/usr/local/include/gtk-2.0/gtk/gtkhscale.h
/usr/local/include/gtk-2.0/gtk/gtkhscrollbar.h
/usr/local/include/gtk-2.0/gtk/gtkhseparator.h
/usr/local/include/gtk-2.0/gtk/gtkiconfactory.h
/usr/local/include/gtk-2.0/gtk/gtkimage.h
/usr/local/include/gtk-2.0/gtk/gtkimagemenuitem.h
/usr/local/include/gtk-2.0/gtk/gtkimcontext.h
/usr/local/include/gtk-2.0/gtk/gtkimcontextsimple.h
/usr/local/include/gtk-2.0/gtk/gtkimmodule.h
/usr/local/include/gtk-2.0/gtk/gtkimmulticontext.h
/usr/local/include/gtk-2.0/gtk/gtkinputdialog.h
/usr/local/include/gtk-2.0/gtk/gtkinvisible.h
/usr/local/include/gtk-2.0/gtk/gtkitem.h
/usr/local/include/gtk-2.0/gtk/gtkitemfactory.h
/usr/local/include/gtk-2.0/gtk/gtklabel.h
/usr/local/include/gtk-2.0/gtk/gtklayout.h
/usr/local/include/gtk-2.0/gtk/gtklist.h
/usr/local/include/gtk-2.0/gtk/gtklistitem.h
/usr/local/include/gtk-2.0/gtk/gtkliststore.h
/usr/local/include/gtk-2.0/gtk/gtkmain.h
/usr/local/include/gtk-2.0/gtk/gtkmarshal.h
/usr/local/include/gtk-2.0/gtk/gtkmenu.h
/usr/local/include/gtk-2.0/gtk/gtkmenubar.h
/usr/local/include/gtk-2.0/gtk/gtkmenuitem.h
/usr/local/include/gtk-2.0/gtk/gtkmenushell.h
/usr/local/include/gtk-2.0/gtk/gtkmessagedialog.h
/usr/local/include/gtk-2.0/gtk/gtkmisc.h
/usr/local/include/gtk-2.0/gtk/gtknotebook.h
/usr/local/include/gtk-2.0/gtk/gtkobject.h
/usr/local/include/gtk-2.0/gtk/gtkoldeditable.h
/usr/local/include/gtk-2.0/gtk/gtkoptionmenu.h
/usr/local/include/gtk-2.0/gtk/gtkpaned.h
/usr/local/include/gtk-2.0/gtk/gtkpixmap.h
/usr/local/include/gtk-2.0/gtk/gtkplug.h
/usr/local/include/gtk-2.0/gtk/gtkpreview.h
/usr/local/include/gtk-2.0/gtk/gtkprivate.h
/usr/local/include/gtk-2.0/gtk/gtkprogress.h
/usr/local/include/gtk-2.0/gtk/gtkprogressbar.h
/usr/local/include/gtk-2.0/gtk/gtkradiobutton.h
/usr/local/include/gtk-2.0/gtk/gtkradiomenuitem.h
/usr/local/include/gtk-2.0/gtk/gtkrange.h
/usr/local/include/gtk-2.0/gtk/gtkrc.h
/usr/local/include/gtk-2.0/gtk/gtkruler.h
/usr/local/include/gtk-2.0/gtk/gtkscale.h
/usr/local/include/gtk-2.0/gtk/gtkscrollbar.h
/usr/local/include/gtk-2.0/gtk/gtkscrolledwindow.h
/usr/local/include/gtk-2.0/gtk/gtkselection.h
/usr/local/include/gtk-2.0/gtk/gtkseparator.h
/usr/local/include/gtk-2.0/gtk/gtkseparatormenuitem.h
/usr/local/include/gtk-2.0/gtk/gtksettings.h
/usr/local/include/gtk-2.0/gtk/gtksignal.h
/usr/local/include/gtk-2.0/gtk/gtksizegroup.h
/usr/local/include/gtk-2.0/gtk/gtksocket.h
/usr/local/include/gtk-2.0/gtk/gtkspinbutton.h
/usr/local/include/gtk-2.0/gtk/gtkstatusbar.h
/usr/local/include/gtk-2.0/gtk/gtkstock.h
/usr/local/include/gtk-2.0/gtk/gtkstyle.h
/usr/local/include/gtk-2.0/gtk/gtktable.h
/usr/local/include/gtk-2.0/gtk/gtktearoffmenuitem.h
/usr/local/include/gtk-2.0/gtk/gtktext.h
/usr/local/include/gtk-2.0/gtk/gtktextbuffer.h
/usr/local/include/gtk-2.0/gtk/gtktextchild.h
/usr/local/include/gtk-2.0/gtk/gtktextdisplay.h
/usr/local/include/gtk-2.0/gtk/gtktextiter.h
/usr/local/include/gtk-2.0/gtk/gtktextlayout.h
/usr/local/include/gtk-2.0/gtk/gtktextmark.h
/usr/local/include/gtk-2.0/gtk/gtktexttag.h
/usr/local/include/gtk-2.0/gtk/gtktexttagtable.h
/usr/local/include/gtk-2.0/gtk/gtktextview.h
/usr/local/include/gtk-2.0/gtk/gtktipsquery.h
/usr/local/include/gtk-2.0/gtk/gtktogglebutton.h
/usr/local/include/gtk-2.0/gtk/gtktoolbar.h
/usr/local/include/gtk-2.0/gtk/gtktooltips.h
/usr/local/include/gtk-2.0/gtk/gtktree.h
/usr/local/include/gtk-2.0/gtk/gtktreednd.h
/usr/local/include/gtk-2.0/gtk/gtktreeitem.h
/usr/local/include/gtk-2.0/gtk/gtktreemodel.h
/usr/local/include/gtk-2.0/gtk/gtktreemodelsort.h
/usr/local/include/gtk-2.0/gtk/gtktreeselection.h
/usr/local/include/gtk-2.0/gtk/gtktreesortable.h
/usr/local/include/gtk-2.0/gtk/gtktreestore.h
/usr/local/include/gtk-2.0/gtk/gtktreeview.h
/usr/local/include/gtk-2.0/gtk/gtktreeviewcolumn.h
/usr/local/include/gtk-2.0/gtk/gtktypebuiltins.h
/usr/local/include/gtk-2.0/gtk/gtktypeutils.h
/usr/local/include/gtk-2.0/gtk/gtkvbbox.h
/usr/local/include/gtk-2.0/gtk/gtkvbox.h
/usr/local/include/gtk-2.0/gtk/gtkversion.h
/usr/local/include/gtk-2.0/gtk/gtkviewport.h
/usr/local/include/gtk-2.0/gtk/gtkvpaned.h
/usr/local/include/gtk-2.0/gtk/gtkvruler.h
/usr/local/include/gtk-2.0/gtk/gtkvscale.h
/usr/local/include/gtk-2.0/gtk/gtkvscrollbar.h
/usr/local/include/gtk-2.0/gtk/gtkvseparator.h
/usr/local/include/gtk-2.0/gtk/gtkwidget.h
/usr/local/include/gtk-2.0/gtk/gtkwindow.h
/usr/local/share/aclocal/gtk-2.0.m4

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-2.0/demo/alphatest.png
/usr/local/share/gtk-2.0/demo/apple-red.png
/usr/local/share/gtk-2.0/demo/appwindow.c
/usr/local/share/gtk-2.0/demo/background.jpg
/usr/local/share/gtk-2.0/demo/button_box.c
/usr/local/share/gtk-2.0/demo/changedisplay.c
/usr/local/share/gtk-2.0/demo/colorsel.c
/usr/local/share/gtk-2.0/demo/dialog.c
/usr/local/share/gtk-2.0/demo/drawingarea.c
/usr/local/share/gtk-2.0/demo/editable_cells.c
/usr/local/share/gtk-2.0/demo/floppybuddy.gif
/usr/local/share/gtk-2.0/demo/gnome-applets.png
/usr/local/share/gtk-2.0/demo/gnome-calendar.png
/usr/local/share/gtk-2.0/demo/gnome-foot.png
/usr/local/share/gtk-2.0/demo/gnome-gimp.png
/usr/local/share/gtk-2.0/demo/gnome-gmush.png
/usr/local/share/gtk-2.0/demo/gnome-gsame.png
/usr/local/share/gtk-2.0/demo/gnu-keys.png
/usr/local/share/gtk-2.0/demo/gtk-logo-rgb.gif
/usr/local/share/gtk-2.0/demo/images.c
/usr/local/share/gtk-2.0/demo/item_factory.c
/usr/local/share/gtk-2.0/demo/list_store.c
/usr/local/share/gtk-2.0/demo/menus.c
/usr/local/share/gtk-2.0/demo/panes.c
/usr/local/share/gtk-2.0/demo/pixbufs.c
/usr/local/share/gtk-2.0/demo/sizegroup.c
/usr/local/share/gtk-2.0/demo/stock_browser.c
/usr/local/share/gtk-2.0/demo/textview.c
/usr/local/share/gtk-2.0/demo/tree_store.c
/usr/local/share/gtk-doc/html/gdk-pixbuf/GdkPixbufLoader.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/apa.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/apas02.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/apas03.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Module-Interface.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-Versioning.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-animation.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-creating.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-file-loading.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-file-saving.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-from-drawables.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-rendering.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-xlib-from-drawables.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-xlib-init.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-xlib-rendering.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf-xlib-rgb.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-gdk-pixbuf.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-inline.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-refcounting.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-scaling.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf-util.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/gdk-pixbuf.devhelp
/usr/local/share/gtk-doc/html/gdk-pixbuf/home.png
/usr/local/share/gtk-doc/html/gdk-pixbuf/index.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/index.sgml
/usr/local/share/gtk-doc/html/gdk-pixbuf/left.png
/usr/local/share/gtk-doc/html/gdk-pixbuf/license.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/right.png
/usr/local/share/gtk-doc/html/gdk-pixbuf/rn01.html
/usr/local/share/gtk-doc/html/gdk-pixbuf/up.png
/usr/local/share/gtk-doc/html/gdk/GdkDisplay.html
/usr/local/share/gtk-doc/html/gdk/GdkDisplayManager.html
/usr/local/share/gtk-doc/html/gdk/GdkScreen.html
/usr/local/share/gtk-doc/html/gdk/X_cursor.png
/usr/local/share/gtk-doc/html/gdk/arrow.png
/usr/local/share/gtk-doc/html/gdk/based_arrow_down.png
/usr/local/share/gtk-doc/html/gdk/based_arrow_up.png
/usr/local/share/gtk-doc/html/gdk/boat.png
/usr/local/share/gtk-doc/html/gdk/bogosity.png
/usr/local/share/gtk-doc/html/gdk/bottom_left_corner.png
/usr/local/share/gtk-doc/html/gdk/bottom_right_corner.png
/usr/local/share/gtk-doc/html/gdk/bottom_side.png
/usr/local/share/gtk-doc/html/gdk/bottom_tee.png
/usr/local/share/gtk-doc/html/gdk/box_spiral.png
/usr/local/share/gtk-doc/html/gdk/center_ptr.png
/usr/local/share/gtk-doc/html/gdk/circle.png
/usr/local/share/gtk-doc/html/gdk/clock.png
/usr/local/share/gtk-doc/html/gdk/coffee_mug.png
/usr/local/share/gtk-doc/html/gdk/cross.png
/usr/local/share/gtk-doc/html/gdk/cross_reverse.png
/usr/local/share/gtk-doc/html/gdk/crosshair.png
/usr/local/share/gtk-doc/html/gdk/diamond_cross.png
/usr/local/share/gtk-doc/html/gdk/dot.png
/usr/local/share/gtk-doc/html/gdk/dotbox.png
/usr/local/share/gtk-doc/html/gdk/double_arrow.png
/usr/local/share/gtk-doc/html/gdk/draft_large.png
/usr/local/share/gtk-doc/html/gdk/draft_small.png
/usr/local/share/gtk-doc/html/gdk/draped_box.png
/usr/local/share/gtk-doc/html/gdk/exchange.png
/usr/local/share/gtk-doc/html/gdk/fleur.png
/usr/local/share/gtk-doc/html/gdk/gdk-Bitmaps-and-Pixmaps.html
/usr/local/share/gtk-doc/html/gdk/gdk-Colormaps-and-Colors.html
/usr/local/share/gtk-doc/html/gdk/gdk-Cursors.html
/usr/local/share/gtk-doc/html/gdk/gdk-Drag-and-Drop.html
/usr/local/share/gtk-doc/html/gdk/gdk-Drawing-Primitives.html
/usr/local/share/gtk-doc/html/gdk/gdk-Event-Structures.html
/usr/local/share/gtk-doc/html/gdk/gdk-Events.html
/usr/local/share/gtk-doc/html/gdk/gdk-Fonts.html
/usr/local/share/gtk-doc/html/gdk/gdk-GdkRGB.html
/usr/local/share/gtk-doc/html/gdk/gdk-General.html
/usr/local/share/gtk-doc/html/gdk/gdk-Graphics-Contexts.html
/usr/local/share/gtk-doc/html/gdk/gdk-Images.html
/usr/local/share/gtk-doc/html/gdk/gdk-Input-Devices.html
/usr/local/share/gtk-doc/html/gdk/gdk-Input.html
/usr/local/share/gtk-doc/html/gdk/gdk-Keyboard-Handling.html
/usr/local/share/gtk-doc/html/gdk/gdk-Pango-Interaction.html
/usr/local/share/gtk-doc/html/gdk/gdk-Pixbufs.html
/usr/local/share/gtk-doc/html/gdk/gdk-Points-Rectangles-and-Regions.html
/usr/local/share/gtk-doc/html/gdk/gdk-Properties-and-Atoms.html
/usr/local/share/gtk-doc/html/gdk/gdk-Selections.html
/usr/local/share/gtk-doc/html/gdk/gdk-Threads.html
/usr/local/share/gtk-doc/html/gdk/gdk-Visuals.html
/usr/local/share/gtk-doc/html/gdk/gdk-Windows.html
/usr/local/share/gtk-doc/html/gdk/gdk-X-Window-System-Interaction.html
/usr/local/share/gtk-doc/html/gdk/gdk.devhelp
/usr/local/share/gtk-doc/html/gdk/gobbler.png
/usr/local/share/gtk-doc/html/gdk/gumby.png
/usr/local/share/gtk-doc/html/gdk/hand1.png
/usr/local/share/gtk-doc/html/gdk/hand2.png
/usr/local/share/gtk-doc/html/gdk/heart.png
/usr/local/share/gtk-doc/html/gdk/home.png
/usr/local/share/gtk-doc/html/gdk/icon.png
/usr/local/share/gtk-doc/html/gdk/index.html
/usr/local/share/gtk-doc/html/gdk/index.sgml
/usr/local/share/gtk-doc/html/gdk/iron_cross.png
/usr/local/share/gtk-doc/html/gdk/left.png
/usr/local/share/gtk-doc/html/gdk/left_ptr.png
/usr/local/share/gtk-doc/html/gdk/left_side.png
/usr/local/share/gtk-doc/html/gdk/left_tee.png
/usr/local/share/gtk-doc/html/gdk/leftbutton.png
/usr/local/share/gtk-doc/html/gdk/ll_angle.png
/usr/local/share/gtk-doc/html/gdk/lr_angle.png
/usr/local/share/gtk-doc/html/gdk/man.png
/usr/local/share/gtk-doc/html/gdk/middlebutton.png
/usr/local/share/gtk-doc/html/gdk/mouse.png
/usr/local/share/gtk-doc/html/gdk/multihead.html
/usr/local/share/gtk-doc/html/gdk/pencil.png
/usr/local/share/gtk-doc/html/gdk/pirate.png
/usr/local/share/gtk-doc/html/gdk/plus.png
/usr/local/share/gtk-doc/html/gdk/question_arrow.png
/usr/local/share/gtk-doc/html/gdk/reference.html
/usr/local/share/gtk-doc/html/gdk/right.png
/usr/local/share/gtk-doc/html/gdk/right_ptr.png
/usr/local/share/gtk-doc/html/gdk/right_side.png
/usr/local/share/gtk-doc/html/gdk/right_tee.png
/usr/local/share/gtk-doc/html/gdk/rightbutton.png
/usr/local/share/gtk-doc/html/gdk/rtl_logo.png
/usr/local/share/gtk-doc/html/gdk/sailboat.png
/usr/local/share/gtk-doc/html/gdk/sb_down_arrow.png
/usr/local/share/gtk-doc/html/gdk/sb_h_double_arrow.png
/usr/local/share/gtk-doc/html/gdk/sb_left_arrow.png
/usr/local/share/gtk-doc/html/gdk/sb_right_arrow.png
/usr/local/share/gtk-doc/html/gdk/sb_up_arrow.png
/usr/local/share/gtk-doc/html/gdk/sb_v_double_arrow.png
/usr/local/share/gtk-doc/html/gdk/shuttle.png
/usr/local/share/gtk-doc/html/gdk/sizing.png
/usr/local/share/gtk-doc/html/gdk/spider.png
/usr/local/share/gtk-doc/html/gdk/spraycan.png
/usr/local/share/gtk-doc/html/gdk/star.png
/usr/local/share/gtk-doc/html/gdk/target.png
/usr/local/share/gtk-doc/html/gdk/tcross.png
/usr/local/share/gtk-doc/html/gdk/top_left_arrow.png
/usr/local/share/gtk-doc/html/gdk/top_left_corner.png
/usr/local/share/gtk-doc/html/gdk/top_right_corner.png
/usr/local/share/gtk-doc/html/gdk/top_side.png
/usr/local/share/gtk-doc/html/gdk/top_tee.png
/usr/local/share/gtk-doc/html/gdk/trek.png
/usr/local/share/gtk-doc/html/gdk/ul_angle.png
/usr/local/share/gtk-doc/html/gdk/umbrella.png
/usr/local/share/gtk-doc/html/gdk/up.png
/usr/local/share/gtk-doc/html/gdk/ur_angle.png
/usr/local/share/gtk-doc/html/gdk/watch.png
/usr/local/share/gtk-doc/html/gdk/xterm.png
/usr/local/share/gtk-doc/html/gtk/AbstractObjects.html
/usr/local/share/gtk-doc/html/gtk/ButtonWidgets.html
/usr/local/share/gtk-doc/html/gtk/DeprecatedObjects.html
/usr/local/share/gtk-doc/html/gtk/DisplayWidgets.html
/usr/local/share/gtk-doc/html/gtk/GtkAccelLabel.html
/usr/local/share/gtk-doc/html/gtk/GtkAccessible.html
/usr/local/share/gtk-doc/html/gtk/GtkAdjustment.html
/usr/local/share/gtk-doc/html/gtk/GtkAlignment.html
/usr/local/share/gtk-doc/html/gtk/GtkArrow.html
/usr/local/share/gtk-doc/html/gtk/GtkAspectFrame.html
/usr/local/share/gtk-doc/html/gtk/GtkBin.html
/usr/local/share/gtk-doc/html/gtk/GtkBox.html
/usr/local/share/gtk-doc/html/gtk/GtkButton.html
/usr/local/share/gtk-doc/html/gtk/GtkButtonBox.html
/usr/local/share/gtk-doc/html/gtk/GtkCList.html
/usr/local/share/gtk-doc/html/gtk/GtkCTree.html
/usr/local/share/gtk-doc/html/gtk/GtkCalendar.html
/usr/local/share/gtk-doc/html/gtk/GtkCellEditable.html
/usr/local/share/gtk-doc/html/gtk/GtkCellRenderer.html
/usr/local/share/gtk-doc/html/gtk/GtkCellRendererPixbuf.html
/usr/local/share/gtk-doc/html/gtk/GtkCellRendererText.html
/usr/local/share/gtk-doc/html/gtk/GtkCellRendererToggle.html
/usr/local/share/gtk-doc/html/gtk/GtkCheckButton.html
/usr/local/share/gtk-doc/html/gtk/GtkCheckMenuItem.html
/usr/local/share/gtk-doc/html/gtk/GtkColorSelection.html
/usr/local/share/gtk-doc/html/gtk/GtkColorSelectionDialog.html
/usr/local/share/gtk-doc/html/gtk/GtkCombo.html
/usr/local/share/gtk-doc/html/gtk/GtkContainer.html
/usr/local/share/gtk-doc/html/gtk/GtkCurve.html
/usr/local/share/gtk-doc/html/gtk/GtkDialog.html
/usr/local/share/gtk-doc/html/gtk/GtkDrawingArea.html
/usr/local/share/gtk-doc/html/gtk/GtkEditable.html
/usr/local/share/gtk-doc/html/gtk/GtkEntry.html
/usr/local/share/gtk-doc/html/gtk/GtkEventBox.html
/usr/local/share/gtk-doc/html/gtk/GtkFileSelection.html
/usr/local/share/gtk-doc/html/gtk/GtkFixed.html
/usr/local/share/gtk-doc/html/gtk/GtkFontSelection.html
/usr/local/share/gtk-doc/html/gtk/GtkFontSelectionDialog.html
/usr/local/share/gtk-doc/html/gtk/GtkFrame.html
/usr/local/share/gtk-doc/html/gtk/GtkGammaCurve.html
/usr/local/share/gtk-doc/html/gtk/GtkHBox.html
/usr/local/share/gtk-doc/html/gtk/GtkHButtonBox.html
/usr/local/share/gtk-doc/html/gtk/GtkHPaned.html
/usr/local/share/gtk-doc/html/gtk/GtkHRuler.html
/usr/local/share/gtk-doc/html/gtk/GtkHScale.html
/usr/local/share/gtk-doc/html/gtk/GtkHScrollbar.html
/usr/local/share/gtk-doc/html/gtk/GtkHSeparator.html
/usr/local/share/gtk-doc/html/gtk/GtkHandleBox.html
/usr/local/share/gtk-doc/html/gtk/GtkIMContext.html
/usr/local/share/gtk-doc/html/gtk/GtkIMContextSimple.html
/usr/local/share/gtk-doc/html/gtk/GtkIMMulticontext.html
/usr/local/share/gtk-doc/html/gtk/GtkImage.html
/usr/local/share/gtk-doc/html/gtk/GtkImageMenuItem.html
/usr/local/share/gtk-doc/html/gtk/GtkInputDialog.html
/usr/local/share/gtk-doc/html/gtk/GtkInvisible.html
/usr/local/share/gtk-doc/html/gtk/GtkItem.html
/usr/local/share/gtk-doc/html/gtk/GtkItemFactory.html
/usr/local/share/gtk-doc/html/gtk/GtkLabel.html
/usr/local/share/gtk-doc/html/gtk/GtkLayout.html
/usr/local/share/gtk-doc/html/gtk/GtkList.html
/usr/local/share/gtk-doc/html/gtk/GtkListItem.html
/usr/local/share/gtk-doc/html/gtk/GtkListStore.html
/usr/local/share/gtk-doc/html/gtk/GtkMenu.html
/usr/local/share/gtk-doc/html/gtk/GtkMenuBar.html
/usr/local/share/gtk-doc/html/gtk/GtkMenuItem.html
/usr/local/share/gtk-doc/html/gtk/GtkMenuShell.html
/usr/local/share/gtk-doc/html/gtk/GtkMessageDialog.html
/usr/local/share/gtk-doc/html/gtk/GtkMisc.html
/usr/local/share/gtk-doc/html/gtk/GtkNotebook.html
/usr/local/share/gtk-doc/html/gtk/GtkObject.html
/usr/local/share/gtk-doc/html/gtk/GtkOldEditable.html
/usr/local/share/gtk-doc/html/gtk/GtkOptionMenu.html
/usr/local/share/gtk-doc/html/gtk/GtkPaned.html
/usr/local/share/gtk-doc/html/gtk/GtkPixmap.html
/usr/local/share/gtk-doc/html/gtk/GtkPlug.html
/usr/local/share/gtk-doc/html/gtk/GtkPreview.html
/usr/local/share/gtk-doc/html/gtk/GtkProgress.html
/usr/local/share/gtk-doc/html/gtk/GtkProgressBar.html
/usr/local/share/gtk-doc/html/gtk/GtkRadioButton.html
/usr/local/share/gtk-doc/html/gtk/GtkRadioMenuItem.html
/usr/local/share/gtk-doc/html/gtk/GtkRange.html
/usr/local/share/gtk-doc/html/gtk/GtkRuler.html
/usr/local/share/gtk-doc/html/gtk/GtkScale.html
/usr/local/share/gtk-doc/html/gtk/GtkScrollbar.html
/usr/local/share/gtk-doc/html/gtk/GtkScrolledWindow.html
/usr/local/share/gtk-doc/html/gtk/GtkSeparator.html
/usr/local/share/gtk-doc/html/gtk/GtkSeparatorMenuItem.html
/usr/local/share/gtk-doc/html/gtk/GtkSettings.html
/usr/local/share/gtk-doc/html/gtk/GtkSizeGroup.html
/usr/local/share/gtk-doc/html/gtk/GtkSocket.html
/usr/local/share/gtk-doc/html/gtk/GtkSpinButton.html
/usr/local/share/gtk-doc/html/gtk/GtkStatusbar.html
/usr/local/share/gtk-doc/html/gtk/GtkStyle.html
/usr/local/share/gtk-doc/html/gtk/GtkTable.html
/usr/local/share/gtk-doc/html/gtk/GtkTearoffMenuItem.html
/usr/local/share/gtk-doc/html/gtk/GtkText.html
/usr/local/share/gtk-doc/html/gtk/GtkTextBuffer.html
/usr/local/share/gtk-doc/html/gtk/GtkTextMark.html
/usr/local/share/gtk-doc/html/gtk/GtkTextTag.html
/usr/local/share/gtk-doc/html/gtk/GtkTextTagTable.html
/usr/local/share/gtk-doc/html/gtk/GtkTextView.html
/usr/local/share/gtk-doc/html/gtk/GtkTipsQuery.html
/usr/local/share/gtk-doc/html/gtk/GtkToggleButton.html
/usr/local/share/gtk-doc/html/gtk/GtkToolbar.html
/usr/local/share/gtk-doc/html/gtk/GtkTooltips.html
/usr/local/share/gtk-doc/html/gtk/GtkTree.html
/usr/local/share/gtk-doc/html/gtk/GtkTreeItem.html
/usr/local/share/gtk-doc/html/gtk/GtkTreeModel.html
/usr/local/share/gtk-doc/html/gtk/GtkTreeModelSort.html
/usr/local/share/gtk-doc/html/gtk/GtkTreeSelection.html
/usr/local/share/gtk-doc/html/gtk/GtkTreeSortable.html
/usr/local/share/gtk-doc/html/gtk/GtkTreeStore.html
/usr/local/share/gtk-doc/html/gtk/GtkTreeView.html
/usr/local/share/gtk-doc/html/gtk/GtkTreeViewColumn.html
/usr/local/share/gtk-doc/html/gtk/GtkVBox.html
/usr/local/share/gtk-doc/html/gtk/GtkVButtonBox.html
/usr/local/share/gtk-doc/html/gtk/GtkVPaned.html
/usr/local/share/gtk-doc/html/gtk/GtkVRuler.html
/usr/local/share/gtk-doc/html/gtk/GtkVScale.html
/usr/local/share/gtk-doc/html/gtk/GtkVScrollbar.html
/usr/local/share/gtk-doc/html/gtk/GtkVSeparator.html
/usr/local/share/gtk-doc/html/gtk/GtkViewport.html
/usr/local/share/gtk-doc/html/gtk/GtkWidget.html
/usr/local/share/gtk-doc/html/gtk/GtkWindow.html
/usr/local/share/gtk-doc/html/gtk/GtkWindowGroup.html
/usr/local/share/gtk-doc/html/gtk/LayoutContainers.html
/usr/local/share/gtk-doc/html/gtk/MenusAndCombos.html
/usr/local/share/gtk-doc/html/gtk/MiscObjects.html
/usr/local/share/gtk-doc/html/gtk/NumericEntry.html
/usr/local/share/gtk-doc/html/gtk/Ornaments.html
/usr/local/share/gtk-doc/html/gtk/PlugSocket.html
/usr/local/share/gtk-doc/html/gtk/ScrollingWidgets.html
/usr/local/share/gtk-doc/html/gtk/SelectorWidgets.html
/usr/local/share/gtk-doc/html/gtk/SpecialObjects.html
/usr/local/share/gtk-doc/html/gtk/TextWidget.html
/usr/local/share/gtk-doc/html/gtk/TextWidgetObjects.html
/usr/local/share/gtk-doc/html/gtk/TreeWidget.html
/usr/local/share/gtk-doc/html/gtk/TreeWidgetObjects.html
/usr/local/share/gtk-doc/html/gtk/WindowWidgets.html
/usr/local/share/gtk-doc/html/gtk/ch01.html
/usr/local/share/gtk-doc/html/gtk/gtk-Accelerator-Maps.html
/usr/local/share/gtk-doc/html/gtk/gtk-Bindings.html
/usr/local/share/gtk-doc/html/gtk/gtk-Clipboards.html
/usr/local/share/gtk-doc/html/gtk/gtk-Drag-and-Drop.html
/usr/local/share/gtk-doc/html/gtk/gtk-Feature-Test-Macros.html
/usr/local/share/gtk-doc/html/gtk/gtk-General.html
/usr/local/share/gtk-doc/html/gtk/gtk-Graphics-Contexts.html
/usr/local/share/gtk-doc/html/gtk/gtk-GtkTextIter.html
/usr/local/share/gtk-doc/html/gtk/gtk-GtkTreeView-drag-and-drop.html
/usr/local/share/gtk-doc/html/gtk/gtk-Keyboard-Accelerators.html
/usr/local/share/gtk-doc/html/gtk/gtk-Resource-Files.html
/usr/local/share/gtk-doc/html/gtk/gtk-Selections.html
/usr/local/share/gtk-doc/html/gtk/gtk-Signals.html
/usr/local/share/gtk-doc/html/gtk/gtk-Standard-Enumerations.html
/usr/local/share/gtk-doc/html/gtk/gtk-Stock-Items.html
/usr/local/share/gtk-doc/html/gtk/gtk-Themeable-Stock-Images.html
/usr/local/share/gtk-doc/html/gtk/gtk-Types.html
/usr/local/share/gtk-doc/html/gtk/gtk-building.html
/usr/local/share/gtk-doc/html/gtk/gtk-changes-1-2.html
/usr/local/share/gtk-doc/html/gtk/gtk-changes-2-0.html
/usr/local/share/gtk-doc/html/gtk/gtk-compiling.html
/usr/local/share/gtk-doc/html/gtk/gtk-framebuffer.html
/usr/local/share/gtk-doc/html/gtk/gtk-question-index.html
/usr/local/share/gtk-doc/html/gtk/gtk-resources.html
/usr/local/share/gtk-doc/html/gtk/gtk-running.html
/usr/local/share/gtk-doc/html/gtk/gtk-windows.html
/usr/local/share/gtk-doc/html/gtk/gtk-x11.html
/usr/local/share/gtk-doc/html/gtk/gtk.devhelp
/usr/local/share/gtk-doc/html/gtk/gtk.html
/usr/local/share/gtk-doc/html/gtk/gtkbase.html
/usr/local/share/gtk-doc/html/gtk/gtkobjects.html
/usr/local/share/gtk-doc/html/gtk/home.png
/usr/local/share/gtk-doc/html/gtk/index.html
/usr/local/share/gtk-doc/html/gtk/index.sgml
/usr/local/share/gtk-doc/html/gtk/left.png
/usr/local/share/gtk-doc/html/gtk/right.png
/usr/local/share/gtk-doc/html/gtk/stock_add_24.png
/usr/local/share/gtk-doc/html/gtk/stock_align_center_24.png
/usr/local/share/gtk-doc/html/gtk/stock_align_justify_24.png
/usr/local/share/gtk-doc/html/gtk/stock_align_left_24.png
/usr/local/share/gtk-doc/html/gtk/stock_align_right_24.png
/usr/local/share/gtk-doc/html/gtk/stock_apply_20.png
/usr/local/share/gtk-doc/html/gtk/stock_bottom_24.png
/usr/local/share/gtk-doc/html/gtk/stock_broken_image_24.png
/usr/local/share/gtk-doc/html/gtk/stock_cancel_20.png
/usr/local/share/gtk-doc/html/gtk/stock_cdrom_24.png
/usr/local/share/gtk-doc/html/gtk/stock_clear_24.png
/usr/local/share/gtk-doc/html/gtk/stock_close_24.png
/usr/local/share/gtk-doc/html/gtk/stock_colorselector_24.png
/usr/local/share/gtk-doc/html/gtk/stock_convert_24.png
/usr/local/share/gtk-doc/html/gtk/stock_copy_24.png
/usr/local/share/gtk-doc/html/gtk/stock_cut_24.png
/usr/local/share/gtk-doc/html/gtk/stock_dialog_error_48.png
/usr/local/share/gtk-doc/html/gtk/stock_dialog_info_48.png
/usr/local/share/gtk-doc/html/gtk/stock_dialog_question_48.png
/usr/local/share/gtk-doc/html/gtk/stock_dialog_warning_48.png
/usr/local/share/gtk-doc/html/gtk/stock_dnd_32.png
/usr/local/share/gtk-doc/html/gtk/stock_dnd_multiple_32.png
/usr/local/share/gtk-doc/html/gtk/stock_down_arrow_24.png
/usr/local/share/gtk-doc/html/gtk/stock_exec_24.png
/usr/local/share/gtk-doc/html/gtk/stock_exit_24.png
/usr/local/share/gtk-doc/html/gtk/stock_first_24.png
/usr/local/share/gtk-doc/html/gtk/stock_font_24.png
/usr/local/share/gtk-doc/html/gtk/stock_help_24.png
/usr/local/share/gtk-doc/html/gtk/stock_home_24.png
/usr/local/share/gtk-doc/html/gtk/stock_index_24.png
/usr/local/share/gtk-doc/html/gtk/stock_jump_to_24.png
/usr/local/share/gtk-doc/html/gtk/stock_last_24.png
/usr/local/share/gtk-doc/html/gtk/stock_left_arrow_24.png
/usr/local/share/gtk-doc/html/gtk/stock_new_24.png
/usr/local/share/gtk-doc/html/gtk/stock_no_20.png
/usr/local/share/gtk-doc/html/gtk/stock_ok_20.png
/usr/local/share/gtk-doc/html/gtk/stock_open_24.png
/usr/local/share/gtk-doc/html/gtk/stock_paste_24.png
/usr/local/share/gtk-doc/html/gtk/stock_preferences_24.png
/usr/local/share/gtk-doc/html/gtk/stock_print_24.png
/usr/local/share/gtk-doc/html/gtk/stock_print_preview_24.png
/usr/local/share/gtk-doc/html/gtk/stock_properties_24.png
/usr/local/share/gtk-doc/html/gtk/stock_redo_24.png
/usr/local/share/gtk-doc/html/gtk/stock_refresh_24.png
/usr/local/share/gtk-doc/html/gtk/stock_remove_24.png
/usr/local/share/gtk-doc/html/gtk/stock_revert_24.png
/usr/local/share/gtk-doc/html/gtk/stock_right_arrow_24.png
/usr/local/share/gtk-doc/html/gtk/stock_save_24.png
/usr/local/share/gtk-doc/html/gtk/stock_save_as_24.png
/usr/local/share/gtk-doc/html/gtk/stock_search_24.png
/usr/local/share/gtk-doc/html/gtk/stock_search_replace_24.png
/usr/local/share/gtk-doc/html/gtk/stock_sort_ascending_24.png
/usr/local/share/gtk-doc/html/gtk/stock_sort_descending_24.png
/usr/local/share/gtk-doc/html/gtk/stock_spellcheck_24.png
/usr/local/share/gtk-doc/html/gtk/stock_stop_24.png
/usr/local/share/gtk-doc/html/gtk/stock_text_bold_24.png
/usr/local/share/gtk-doc/html/gtk/stock_text_italic_24.png
/usr/local/share/gtk-doc/html/gtk/stock_text_strikethrough_24.png
/usr/local/share/gtk-doc/html/gtk/stock_text_underline_24.png
/usr/local/share/gtk-doc/html/gtk/stock_top_24.png
/usr/local/share/gtk-doc/html/gtk/stock_trash_24.png
/usr/local/share/gtk-doc/html/gtk/stock_undelete_24.png
/usr/local/share/gtk-doc/html/gtk/stock_undo_24.png
/usr/local/share/gtk-doc/html/gtk/stock_up_arrow_24.png
/usr/local/share/gtk-doc/html/gtk/stock_yes_20.png
/usr/local/share/gtk-doc/html/gtk/stock_zoom_1_24.png
/usr/local/share/gtk-doc/html/gtk/stock_zoom_fit_24.png
/usr/local/share/gtk-doc/html/gtk/stock_zoom_in_24.png
/usr/local/share/gtk-doc/html/gtk/stock_zoom_out_24.png
/usr/local/share/gtk-doc/html/gtk/up.png
