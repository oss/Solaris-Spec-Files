Summary: Common SGML catalog and DTD files.
Name: sgml-common
%define version 0.1
%define release 7
Version: %{version}
Release: %{release}
Source: ftp://sourceware.cygnus.com/pub/docbook-tools/SOURCES/sgml-common.tgz
Copyright: freely distributable
Group: Applications/Text
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-root
Prefix: /usr/local

%description
The sgml-common package contains a collection of entities and DTDs
that are useful for processing SGML, but that don't need to be
included in multiple packages.  Sgml-common also includes an
up-to-date Open Catalog file.

%prep
%setup -c
%build
gawk --posix '/Typical invocation:/,/\-\-\>/ { print }' sgml-common/* |
gawk --posix '/PUBLIC/ { sys=$3 } 
	/8879:1986.*\"\>/ { saveline=""; print "PUBLIC " $0 " " sys; next }
	/8879:1986[^>]*$/ { saveline = $0; next }
	/\"\>/ { print "PUBLIC " saveline  $0 " " sys; saveline="";next }
' |
sed 's/\">/\"/' > newcat

cat > install-catalog << '__EOF__'
#!/bin/sh
set -e
sgmlbase=%{prefix}/lib/sgml
state=""
package=""
version=""

for i in $*; do
  case $state in 
	"")
	  case $i in
	  --install) state="--install" ; action="install";;
	  --remove) state="--remove"   ; action="remove";;
	  --sgmlbase) state="--sgmlbase" ;;
	  --version) state="--version" ;;
	  *) cat <<__USAGE__
Usage:
 --install pkg:		installs pkg.cat in CATALOG
 --remove pkg:		removes pkg.cat from CATALOG
 --version ver:		qualify version of package
 --sgmlbase path:	changes directory for pkg.cat and CATALOG
__USAGE__
 exit 0
 ;;
	  esac
	;;
	--install) state="" ; package=$i ;; 
	--remove) state="" ; package=$i ;;
	--sgmlbase) state="" ; sgmlbase=$i;;
	--version) state="" ; version=$i ;;
  esac
done

echo "install-catalog: $action of $package DTD"

cat=$sgmlbase/CATALOG

SBEG=" -- start $package $version"
SEND=" -- end $package $version"

case $action in
  install)
	if grep "$SBEG" $cat
	then
	  echo "$package DTD already in catalog"
	else
	  echo "adding $package DTD to catalog"
	(echo "$SBEG -- "; 
	 cat $sgmlbase/$package.cat ;
	 echo "$SEND -- ") >> $cat
	fi
  ;;
  remove)
	if grep "$SBEG" $cat
	then
	  echo "removing $package$version DTD from catalog"
          sed -e "/$SBEG/,/$SEND/d" < $cat > ${cat}.new
                mv ${cat}.new ${cat}
	else
	  echo "No $package$version DTD found in catalog"
	fi
  ;;
  *) echo "install-catalog: Invalid action $action"; exit 1 ;;
esac
__EOF__
chmod +x install-catalog

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{prefix}/bin
mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib/sgml

install sgml-common/* $RPM_BUILD_ROOT/%{prefix}/lib/sgml
install newcat $RPM_BUILD_ROOT/%{prefix}/lib/sgml/sgml-common.cat

install -m 755 install-catalog $RPM_BUILD_ROOT/%{prefix}/bin

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch %{prefix}/lib/sgml/CATALOG
chmod 0644 %{prefix}/lib/sgml/CATALOG
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{prefix}/bin/install-catalog --install sgml-common --version $V >/dev/null

%postun
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{prefix}/bin/install-catalog --remove sgml-common --version $V >/dev/null

%files
%defattr(-,root,root)
%{prefix}/lib/sgml/*
%{prefix}/bin/install-catalog

%changelog
* Wed Jan  5 2000 Bill Nottingham <notting@redhat.com>
- sanitize spec file some

* Mon Aug 30 1999 Tim Powers <timp@redhat.com>
- changed group
- changed buildroot to be in /var/tmp

* Wed Jul 21 1999 Tim Powsrs <timp@redhat.com>
- rebuilt for 6.1

* Fri Apr 23 1999 Michael K. Johnson <johnsonm@redhat.com>
- quiet scripts

* Thu Apr 22 1999 Owen Taylor <otaylor@redhat.com>
- Made noarch
