Name: Xaw3d
Version: 1.5
Release: 3
Summary: 3D Athena widgets for X
Group: User Interface/X
Copyright: BSD-type
Provides: libXaw3d.so
Source0: Xaw3d-1.5.tar.gz
Source1: Xaw3d-extras.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Xaw3d is a replacement for Xaw (the Athena toolkit) that looks nicer.
Simply linking with -lXaw3d instead of -lXaw increases eye-candy by an
order of magnitude.  Install this package if you need libXaw3d.

%prep
%setup -q -n xc/lib/Xaw3d
%setup -D -T -a 1 -n xc/lib/Xaw3d
ln -s `pwd` X11/Xaw3d
perl -i -p -e 's/^#\ *EXTRA_INCLUDES/EXTRA_INCLUDES/' Imakefile

%build
xmkmf -a
make CC=gcc PICFLAGS="-fpic" CCOPTIONS="-O -I."

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/include/X11/Xaw3d
mkdir $RPM_BUILD_ROOT/usr/local/lib
install -c -m 0644 libXaw3d.so.5 $RPM_BUILD_ROOT/usr/local/lib
for i in AllWidgets.h AsciiSink.h AsciiSinkP.h AsciiSrc.h AsciiSrcP.h AsciiText.h AsciiTextP.h Box.h BoxP.h Cardinals.h Command.h CommandP.h Dialog.h DialogP.h Form.h FormP.h Grip.h GripP.h Label.h LabelP.h Layout.h LayoutP.h List.h ListP.h MenuButton.h MenuButtoP.h MultiSrc.h MultiSrcP.h MultiSink.h MultiSinkP.h Paned.h PanedP.h Panner.h PannerP.h Porthole.h PortholeP.h Repeater.h RepeaterP.h Reports.h Scrollbar.h ScrollbarP.h Simple.h SimpleP.h SimpleMenu.h SimpleMenP.h Sme.h SmeP.h SmeBSB.h SmeBSBP.h SmeLine.h SmeLineP.h SmeThreeD.h SmeThreeDP.h StripChart.h StripCharP.h Template.c Template.h TemplateP.h Text.h TextP.h TextSink.h TextSinkP.h TextSrc.h TextSrcP.h ThreeD.h ThreeDP.h Toggle.h ToggleP.h Tree.h TreeP.h VendorEP.h Viewport.h ViewportP.h XawImP.h XawInit.h ; do
    install -c -m 0644 $i $RPM_BUILD_ROOT/usr/local/include/X11/Xaw3d
done
cd $RPM_BUILD_ROOT/usr/local/lib
ln -s libXaw3d.so.5 libXaw3d.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README.XAW3D
/usr/local/lib/lib*.so*
/usr/local/include/X11/Xaw3d

