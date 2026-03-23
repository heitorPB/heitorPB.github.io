window.wander = {
  // Other Wander consoles that visitors can reach from my console.
  consoles: [
    'https://susam.net/wander/',
    'https://tuftel.today/wander/',
    'https://martincapodici.com/wander/'
  ],
  // My favourite websites and pages I recommend to the Wander community.
  pages: [
    'https://susam.net/',
    'https://sunshowers.io/',
    'https://julianaklulo.dev/en/',
    'https://jvns.ca/',
    'https://discord.com/blog/why-discord-is-switching-from-go-to-rust'
  ],
  // Websites and consoles to ignore. My console will never fetch consoles or
  // web pages whose URLs match the following patterns.
  ignore: [
    // Out of scope. These are commercial platforms, not personal websites.
    'https://medium.com/',
    'https://substack.com/',

    // These pages fail to load in the console due to frame restrictions.
    'https://cari.institute/',
    'https://wdl.mcdaniel.edu/',
  ]
}
