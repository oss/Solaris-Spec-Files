%define apver 1.3.29

Summary: A Photo Gallery Module for Apache
Name: mod_coolphoto
Version: 2.0
Release: 1
Group: Applications/Internet
License: Unknown
Source0: mod_coolphoto.2.0.tar.gz
Source1: mod_coolphoto.buttons.tar.gz
BuildRoot: /var/tmp/%{name}-root

%define apache_prefix /usr/local/apache-%{apver}

BuildRequires: apache = %{apver} apache-devel = %{apver} freetype2-devel mm-devel zlib-devel libpng3-devel bzip2 libtiff-devel 
Requires: apache freetype2 mm zlib libpng3 bzip2 libtiff 

%description
lphoto is an Apache module that enables you to manage and display images
within a series of photo galleries. It has been written and tested using
Linux and Apache 1.3x. Each virtual server on the machine can have its own
configuration and its own unique galleries.

%prep
%setup -q -n mod_coolphoto-%{version} -a 0
%setup -q -n mod_coolphoto-%{version} -a 1

%build
PATH=%{apache_prefix}/bin:/usr/ccs/bin:$PATH
export PATH

%{apache_prefix}/bin/apxs -l Magick -l mm -l z -l tiff -l png -l bz2 -l freetype -L /usr/local/lib -Wl,-R/usr/local/lib -c mod_coolphoto.c

echo "..... mod_coolphoto configuration instructions .....

Besides the proprietary coolphoto configuration directives listed below,
the only other httpd.conf configuration required is to add appropriate
SetHandler directives in order for mod_coolphoto to execute.

mod_coolphoto is interfaced using two modes: Normal mode and
Administrative mode. Normal mode is the way casual users view your photo
galleries; they can navigate through all the galleries, as well as the
images within those galleries. Administrative mode is reserved for the
administrator of the photo galleries; within this mode images can be
imported, moved around, resized or flipped, and deleted. Due to this
fact, Administrative mode should be password protected. The apache handlers
for Normal and Administrative modes are "cool-photo" and 
"cool-photo-admin", respectively.

The following entry into httpd.conf (usable at the global server or
virtual server level) will set the url for normal viewing of
mod_coolphoto as "http://servername.com/photos":

<Location /photos>
    SetHandler cool-photo
</Location>

Likewise, the following entry into httpd.conf will set the url for the
administrative interface of mod_coolphoto as
"http://servername.com/photoadmin", using Basic Authentication and
requiring the user be authenticated as a member of the "photo-admin"
group (for more information, see the documentation for the AuthType
directive):

<Location /photoadmin>
    SetHandler cool-photo-admin
    AuthName   "Photo Administration"
    AuthType   Basic
    Require    group photo-admin
</Location>

Besides this apache handler configuration, the only other required
directives are coolphoto_enable, coolphoto_config, and coolphoto_depot
(configurable at the global server or virtual server level). All other
directives are optional.

" >> mod_coolphoto-install.txt

%install
mkdir -p /var/tmp/%{name}-root/usr/local/apache-modules/
mkdir -p /var/tmp/%{name}-root/usr/local/share/mod_coolphoto
mkdir -p /var/tmp/%{name}-root/usr/local/share/mod_coolphoto/buttons
cp mod_coolphoto.so /var/tmp/%{name}-root/usr/local/apache-modules/
cp mod_coolphoto-install.txt /var/tmp/%{name}-root/usr/local/share/mod_coolphoto
cp mod_coolphoto-2.0/*.jpg /var/tmp/%{name}-root/usr/local/share/mod_coolphoto/buttons 

%post
cat << EOF 

Besides the proprietary coolphoto configuration directives listed below,
the only other httpd.conf configuration required is to add appropriate
SetHandler directives in order for mod_coolphoto to execute.

mod_coolphoto is interfaced using two modes: Normal mode and
Administrative mode. Normal mode is the way casual users view your photo
galleries; they can navigate through all the galleries, as well as the
images within those galleries. Administrative mode is reserved for the
administrator of the photo galleries; within this mode images can be
imported, moved around, resized or flipped, and deleted. Due to this
fact, Administrative mode should be password protected. The apache handlers
for Normal and Administrative modes are "cool-photo" and 
"cool-photo-admin", respectively.

The following entry into httpd.conf (usable at the global server or
virtual server level) will set the url for normal viewing of
mod_coolphoto as "http://servername.com/photos":

<Location /photos>
    SetHandler cool-photo
</Location>

Likewise, the following entry into httpd.conf will set the url for the
administrative interface of mod_coolphoto as
"http://servername.com/photoadmin", using Basic Authentication and
requiring the user be authenticated as a member of the "photo-admin"
group (for more information, see the documentation for the AuthType
directive):

<Location /photoadmin>
    SetHandler cool-photo-admin
    AuthName   "Photo Administration"
    AuthType   Basic
    Require    group photo-admin
</Location>

Besides this apache handler configuration, the only other required
directives are coolphoto_enable, coolphoto_config, and coolphoto_depot
(configurable at the global server or virtual server level). All other
directives are optional.


*** Buttons are installed in /usr/local/share/mod_coolphoto/buttons

EOF

%files
%defattr(-,root,other)
/usr/local/share/mod_coolphoto/mod_coolphoto-install.txt
/usr/local/apache-modules/mod_coolphoto.so
/usr/local/share/mod_coolphoto/buttons/*.jpg
