Summary: Mime-types and mailcap pkg for netscape and pine 
Name: mime-types
Version: 1.0
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: %{name}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
A more standardized way of getting mime-types and mailcaps.
 
NOTE:

This package contains a postinstall script which will check for the
existence of:
        /usr/local/etc/mailcap
        /usr/local/etc/mime-types exists

If so, it will copy the files mailcap.sample and mime-types.sample to
their respective locations.  If not, the package will simply those
files in /usr/local/etc.

Also, this postinstall script will check for links in
/usr/local/lib/netscape.
   
If the mailcap and/or mime-types file exists in
/usr/local/lib/netscape, the following commands will be executed:
   
        ln -s /usr/local/etc/mailcap.sample /usr/local/lib/netscape/mailcap.samp
le
        ln -s /usr/local/etc/mime-types.sample /usr/local/lib/netscape/mime-type
s.sample

Otherwise these commands will be executed

        ln -s /usr/local/etc/mailcap /usr/local/lib/netscape/mailcap
        ln -s /usr/local/etc/mime-types /usr/local/lib/netscape/mime-types

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%post
DIR="/usr/local/etc";
NDIR="/usr/local/lib/netscape";

###
# does /usr/local/etc/mailcap and /usr/local/etc/mime.types exist?
# if not, copy examples over
#
if [ ! -f "$DIR/mailcap" -a "$DIR/mime.types" ]
then
    echo "$DIR/mailcap does not exist.  Copying $DIR/mailcap.example to $DIR/mai
lcap"
    cp -p $DIR/mailcap.example $DIR/mailcap
    echo "$DIR/mime.types does not exist.  Copying $DIR/mime.types.example to $D
IR/mime.types"
    cp -p $DIR/mime.types.example $DIR/mime.types
else
    echo "$DIR/mailcap and $DIR/mime.types already exist.."

    echo "To replace current $DIR/mailcap with default,"
    echo "   move $DIR/mailcap.example to $DIR/mailcap"

    echo "To replace current $DIR/mime.types with default,"
    echo "   move $DIR/mime.types.example to $DIR/mime.types"
fi


if [ -d "$NDIR" ]
then
    echo "Making $NDIR"
    mkdir $NDIR
    chmod 755 $NDIR
    chown root $NDIR
    chgrp other $NDIR
fi

###
# does /usr/local/lib/netscape/mailcap and mime.types exist?
# if not, then make a link to /usr/local/etc/mailcap and mime.types
# if so, then leave it alone
#

if [ ! -f "$NDIR/mailcap" -a "$NDIR/mime.types" ]
then
    echo "Linking $DIR/mailcap to $NDIR/mailcap"
    ln -s $DIR/mailcap $NDIR/mailcap

    echo "Linking $DIR/mime.types to $NDIR/mime.types"
    ln -s $DIR/mime.types $NDIR/mime.types
else
    echo "$NDIR/mailcap and $NDIR/mime.types file exist"
    echo "To replace existing $NDIR/mailcap and $NDIR/mime.types"
    echo "   with the default files, move $NDIR/mailcap and $NDIR/mime.types"
    echo "   somewhere else and run the following commands:"
    echo "      ln -s $DIR/mailcap $NDIR/mailcap"
    echo "      ln -s $DIR/mime.types $NDIR/mime.types"
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/etc/*
