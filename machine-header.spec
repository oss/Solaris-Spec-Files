# Any RPM with machine-dependent filenames should include this header.

%ifos solaris2.9
%define sol_os      solaris2.9
%ifarch sparc64
%define max_bits    64
%else
%define max_bits    32
%endif
%endif

%ifos solaris2.8
%define sol_os      solaris2.8
%ifarch sparc64
%define max_bits    64
%else
%define max_bits    32
%endif
%endif

%ifarch sparc64
%define real_arch   sparc64-sun-%{sol_os}
%else
%define real_arch   sparc-sun-%{sol_os}
%endif

# Set these to SOLARIS if you want to use the ones bundled with
# Solaris or otherwise provided by Sun:

# For which_perl, we currently use the following setup:
# Solaris8	REPOSITORY
# Solaris9	SOLARIS

%ifos solaris2.8
%define which_perl  REPOSITORY
%else
%define which_perl  SOLARIS
%endif

# We are using Solaris' GNOME
%define which_gnome SOLARIS

# Don't forget to use the correct profile with build-r.pl!

