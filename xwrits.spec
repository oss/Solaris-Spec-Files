Summary: Reminds you to take wrist breaks
Name: xwrits
Version: 2.15
Release: 2
Group: Applications/Productivity
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Xwrits reminds you to take wrist breaks for prevention or management
of repetitive stress injuries. When you should take a break, it pops
up an X window, the warning window.  You click on the warning window,
then take a break. The window changes appearance while you take the
break. It changes again when your break is over. Then you just resume
typing.  Xwrits hides itself until you should take another break.

It is easy to put the warning window aside ``for 5 minutes'' and
ignore it for fifty. Xwrits can escalate its activity over time,
making it harder to ignore.
 (from the manpage)

Xwrits has the capability to be multiculturally rude -- if you specify
+finger[=culture] on the command line, it can display Korean,
Japanese, Russian, German or American obscene hand gestures when it is
time to break.  In addition to the regular binary, this package
contains a "clean" version of xwrits that was not built with rude
gestures.  If you are installing this software publicly and you don't
want users to be able to display rude gestures, run

  mv /usr/local/bin/xwrits.rude_gestures_are_not_funny /usr/local/bin/xwrits

You may also wish to delete /usr/local/doc/xwrits-%{version}/GESTURES.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make
mv xwrits xwrits.obscene
make clean

# censor_gesture replaces gesture $2 with $3 in directory $1.

censor_gesture () {
    if [ $# != "3" ] ; then
	echo censor_gesture error
        exit 1
    elif [ -r "$1/$2.gif" ] ; then
        rm -f "$1/$2.gif"
	cp -p "$1/$3.gif" "$1/$2.gif"
    fi
}

for i in finger german korean ; do
    censor_gesture color ${i}i clenchi
    censor_gesture color ${i}l clenchl
    censor_gesture mono ${i}im clenchim
    censor_gesture mono ${i}lm  clenchlm
done
make

%install
umask 022
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/usr/local/bin/xwrits \
   $RPM_BUILD_ROOT/usr/local/bin/xwrits.rude_gestures_are_not_funny
install -m 0755 xwrits.obscene $RPM_BUILD_ROOT/usr/local/bin/xwrits

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

Xwrits has the capability to be multiculturally rude -- if you specify
+finger[=culture] on the command line, it can display Korean,
Japanese, Russian, German or American obscene hand gestures when it is
time to break.  In addition to the regular binary, this package
contains a "clean" version of xwrits that was not built with rude
gestures.  If you are installing this software publicly and you don't
want users to be able to display rude gestures, run

  mv /usr/local/bin/xwrits.rude_gestures_are_not_funny /usr/local/bin/xwrits

You may also wish to delete /usr/local/doc/xwrits-%{version}/GESTURES.

EOF

%files
%defattr(-,root,other)
%doc GESTURES NEWS README
/usr/local/man/man1/xwrits.1
/usr/local/bin/*
