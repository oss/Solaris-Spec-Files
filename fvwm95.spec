%define fvwm_libdir /usr/local/lib/X11/fvwm95

Summary: Windows 95-style window manager for X
Name: fvwm95
Version: 2.0.43a
Release: 1ru
Group: User Interface/X11
Copyright: BSD-style
Source: fvwm95-%{version}-Autoconf.tgz
BuildRoot: %{_tmppath}/%{name}-root
Requires: xpm
BuildRequires: xpm

%description
FVWM95 is a Windows 95-workalike window manager for X11.

%prep
%setup -q -n %{name}-%{version}-Autoconf

%build
./configure --prefix=/usr/local \
   --with-xpm-library=/usr/local/lib --with-xpm-includes=/usr/local/include
make CC="gcc -L/usr/local/lib -R/usr/local/lib"

%install
SOURCE_ROOT=`pwd`
installbr () {
    dest=$1
    shift
    /usr/local/gnu/bin/install $@ %{buildroot}$dest
}

rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/local/lib \
         %{buildroot}%{fvwm_libdir} %{buildroot}/usr/local/icons \
	 %{buildroot}/usr/local/man/man1

cd $SOURCE_ROOT/fvwm
installbr /usr/local/bin -c fvwm95
installbr /usr/local/man/man1/fvwm95.1 -c -m 0644 fvwm95.man

cd $SOURCE_ROOT/libs
installbr /usr/local/lib -c -m 644 libfvwm95.a

for i in $SOURCE_ROOT/modules/Fvwm*; do
    cd $i
    name=`basename $i`
    [ $name = "FvwmAudio" ] && continue
    installbr %{fvwm_libdir} -c $name
    installbr /usr/local/man/man1/$name.1 -c $name.man
done

cd $SOURCE_ROOT/utils
for i in fvwmrc_convert quantize_pixmaps ; do
    installbr %{fvwm_libdir} -c $i
done

cd $SOURCE_ROOT
installbr %{fvwm_libdir}/system.fvwm95rc.rpm -c -m 644 example.fvwm95rc

cd $SOURCE_ROOT/xpmroot
installbr /usr/local/bin/xpmroot-fvwm95 -c xpmroot
installbr /usr/local/man/man1/xpmroot-fvwm95.1 -c xpmroot.man

cd $SOURCE_ROOT/icons
for i in Mosaic.xpm arrdown2.xpm arrows2.xpm arrup2.xpm bomb.xpm ccode.icon clamp.xpm colormap.xpm datebook.xpm default.xbm desk.xpm dialog_box.xpm doombig.xpm doomface.xpm editres.xpm eps.xpm exit.xpm flow_chart.xpm folder2.xpm folders.xpm fvwm.bitmap fvwm.xpm fvwm2.xpm fvwm2_big.xpm fvwm3.xpm gnu-animal.xpm graphs.xpm gv.xpm hcode.icon jewelbig.xpm k.xpm k2.xpm lemacs.xpm mag_glass.xpm mail1.xpm mail2.xpm map.xpm math4.xpm mini.audiovol.xpm mini.checkmark.xpm mini.cut.xpm mini.destroy.xpm mini.excl.xpm mini.exit.xpm mini.fvwm.xpm mini.letter.xpm mini.lower.xpm mini.move.xpm mini.netscape.xpm mini.raise.xpm mini.resize.xpm mini.xarchie.xpm mini.xboing.xpm mini.xlock.xpm mini.xpm mini.xterm.xpm mini.zircon.xpm nscape.xpm ocode.icon page.xpm page2.xpm prog.icon ps.xpm question.xpm rbomb.xpm rcalc.xpm rterm.xpm term.xpm textedit.xpm tiff2.xpm toolbox.xpm unknown1.xpm wierd_page3.xpm word_processor.xpm world.xpm xboingbig.xpm xcalc.xpm xemacs.xpm xlock.xpm xman.xpm xpaint.xpm xterm-axp.xpm xterm-blank.xpm xterm-dec.xpm xterm-sgi.xpm xterm-sol.xpm xterm-sun.xpm xterm.xpm xv.xpm xview.xpm Xfm.xpm; do
    installbr /usr/local/icons -c -m 644 $i
done

cd $SOURCE_ROOT/mini-icons
for i in Xfm.xpm bckgnd1.xpm bckgnd3.xpm documents.xpm find1.xpm folder.xpm fvwm-menu.xpm gv.xpm help.xpm linux-menu.xpm mini-arch.xpm mini-ball.xpm mini-bball.xpm mini-bomb.xpm mini-book1.xpm mini-book2.xpm mini-books.xpm mini-briefcase.xpm mini-bug1.xpm mini-bug2.xpm mini-bx2.xpm mini-calc.xpm mini-camera.xpm mini-cat.xpm mini-cave.xpm mini-cd.xpm mini-cdlabel.xpm mini-chinese.xpm mini-clipboard.xpm mini-clock.xpm mini-colors.xpm mini-connect.xpm mini-crosbone.xpm mini-cross.xpm mini-desktop.xpm mini-diff.xpm mini-diskette.xpm mini-display.xpm mini-doc.xpm mini-doc1.xpm mini-dog.xpm mini-edit.xpm mini-espada.xpm mini-exclam.xpm mini-exp.xpm mini-eye.xpm mini-eyes.xpm mini-fax.xpm mini-fdisk.xpm mini-filemgr.xpm mini-folder.xpm mini-font.xpm mini-fractal.xpm mini-frame.xpm mini-ftp.xpm mini-gball.xpm mini-go.xpm mini-gopher.xpm mini-graph.xpm mini-gv.xpm mini-hammer.xpm mini-happy.xpm mini-hdisk.xpm mini-heart.xpm mini-hex.xpm mini-hextris.xpm mini-icons.xpm mini-keyboard.xpm mini-lock.xpm mini-lower.xpm mini-mail.xpm mini-manual.xpm mini-max1.xpm mini-maze.xpm mini-modules.xpm mini-monitor.xpm mini-move.xpm mini-move1.xpm mini-mwm.xpm mini-news.xpm mini-nscape.xpm mini-ofolder.xpm mini-olwm.xpm mini-pager.xpm mini-paint.xpm mini-palette.xpm mini-pdf.xpm mini-pencil.xpm mini-penguin.xpm mini-perf.xpm mini-question.xpm mini-raise.xpm mini-ray.xpm mini-rball.xpm mini-resize.xpm mini-roach.xpm mini-run.xpm mini-sh.xpm mini-sh1.xpm mini-slon.xpm mini-sound.xpm mini-start.xpm mini-stop.xpm mini-telnet.xpm mini-term.xpm mini-tetris.xpm mini-trebol.xpm mini-turn.xpm mini-twm.xpm mini-window.xpm mini-windows.xpm mini-x.xpm mini-x2.xpm mini-xfig.xpm mini-xjewel.xpm mini-xkeycaps.xpm mini-xlander.xpm mini-xmahjongg.xpm mini-xsnow.xpm mini-xv.xpm mini-zoom.xpm nscape.xpm programs.xpm rbomb.xpm rcalc.xpm rterm.xpm run.xpm settings.xpm shutdown.xpm textedit.xpm utilities-menu.xpm wterm.xpm xv.xpm; do
    installbr /usr/local/icons -c -m 644 ./$i 
done

%clean
rm -rf %{buildroot}

%post
cat <<EOF
Edit and move %{fvwm_libdir}/system.fvwm95rc.rpm.
EOF

%files
%defattr(-, root, bin)
%doc docs
/usr/local/bin/*
%{fvwm_libdir}
/usr/local/icons/*
