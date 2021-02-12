Name:           conan
Version:        1.33.1
Release:        1%{?dist}
Summary:        Decentralized, open-source, C/C++ package manager

License:        MIT
URL:            https://github.com/conan-io/%{name}
Source0:        %{URL}/archive/%{VERSION}.zip

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc-c++


%description
Conan is a package manager for C and C++ developers. It is decentralized,
portable, easy to manage binaries, seamless to integrate with build system,
extensible, stable, and with a large and active community.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.md
%doc README.rst
%{_bindir}/%{name}
%{_bindir}/%{name}_build_info
%{_bindir}/%{name}_server
%{python3_sitelib}/%{name}-%{version}-py*.egg-info
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}s/

%changelog
* Fri Feb 12 2021 Sheng Mao <shngmao@gmail.com> 1.33.1-1
- Initial Release
