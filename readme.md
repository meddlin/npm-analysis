# NPM Analysis Utility

This is a learning tool for getting acquainted with analyzing NPM packages.


## Why?

Software supply chain security is more important now than ever. It's easy to 
run a scanner, but what do they do? This utility is intended to be a 
playground for building the basics that create SCA and SBOM tools.

### Inspiration

You can start with these two commands to download NPM packages, and start 
analyzing them.

> `curl $(npm view nextjs dist.tarball) -o outfile.tgz`

> `tar -xvzf outfile.tgz`

I wanted to wrap some automation around these commands, and build something 
useful from there.