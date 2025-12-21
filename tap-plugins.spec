Summary:		Tom's Audio Processing plugins
Name:	tap-plugins
Version:	1.0.1
Release:	1
License:	GPLv2+
Group:	Sound
Url:		https://tomscii.sig7.se/tap-plugins/
# Now on https://git.hq.sig7.se/tap-plugins.git, but no way to download tarballs
Source0:	%{name}-%{version}.tar.gz
# From Debian
Patch0:	tap-plugins-1.0.1-pass-compile-flags-correctly.patch

BuildRequires:	make
%description
TAP-plugins is short for Tom's Audio Processing plugins. It is a bunch of
LADSPA plugins for digital audio processing, intended for use in a
professional DAW environment such as Ardour.

%files
%doc CREDITS COPYING README
%{_libdir}/ladspa/tap_*.so
%{_datadir}/ladspa/rdf/*.rdf

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# There is only a makefile
%set_build_flags
%make_build


%install
%make_install INSTALL_PLUGINS_DIR=%{buildroot}%{_libdir}/ladspa/ \
	INSTALL_LRDF_DIR=%{buildroot}%{_datadir}/ladspa/rdf/ install
