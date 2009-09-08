%define name	tap-plugins
%define version 0.7.0
%define release %mkrel 6

Summary:      	Tom's Audio Processing plugins
Name:         	%{name}
Version:      	%{version}
Release:      	%{release}
License:    	GPL
Group:        	Sound
URL:          	http://tap-plugins.sourceforge.net/
Source0:      	tap-plugins-%{version}.tar.bz2
BuildRoot:    	%{_tmppath}/%{name}-buildroot

%description
TAP-plugins is short for Tom's Audio Processing plugins. It is a bunch
of LADSPA plugins for digital audio processing, intended for use in a
professional DAW environment such as Ardour.

%prep
%setup -q
perl -p -i -e "s/-O3/$RPM_OPT_FLAGS/g" Makefile

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
make INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa/ \
     INSTALL_LRDF_DIR=$RPM_BUILD_ROOT%{_datadir}/ladspa/rdf/ install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS README
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*

