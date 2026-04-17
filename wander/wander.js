const wander = {
  // Other Wander consoles that visitors can reach from my console.
  consoles: [
    'https://susam.net/wander/',
    'https://tuftel.today/wander/',
    'https://martincapodici.com/wander/',
    'https://punkto.org/wander/',
  ],
  // My favourite websites and pages I recommend to the Wander community.
  pages: [
    'https://alexhwoods.com/dont-let-ai-write-for-you/',
    'https://allenpike.com/2022/giving-a-shit/',
    'https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns',
    'https://cbea.ms/git-commit/',
    'https://danielmiessler.com/blog/no-moving-your-ssh-port-isnt-security-by-obscurity',
    'https://heitorpb.github.io',
    'https://julianaklulo.dev/en/',
    'https://jvns.ca/',
    'https://lorentz.app/blog-item.html?id=go-shebang',
    'https://mcfunley.com/choose-boring-technology',
    'https://neil.computer/notes/oh-sorry-i-was-on-mute/',
    'https://ratfactor.com/',
    'https://scottstuff.net/posts/2025/09/30/home-ethernet/',
    'https://se3.ch/',
    'https://simonwillison.net/2022/Nov/6/what-to-blog-about/',
    'https://sunshowers.io/',
    'https://susam.net/',
    'https://taylor.town/',
    'https://thelocalstack.eu/posts/linkedin-identity-verification-privacy/',
    'https://www.amateuraerodynamics.com/2022/02/tuft-testing-how-to-manual.html',
    'https://www.jeffgeerling.com/blog/2026/ptp-wall-clock-impractical-too-precise/',
    'https://マリウス.com/coffee/',
    // 'https://discord.com/blog/why-discord-is-switching-from-go-to-rust', // Discord.com doesn't work inside an iframe :(
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
