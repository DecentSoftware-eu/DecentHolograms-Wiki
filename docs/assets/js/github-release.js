document$.subscribe(async () => {
    function loadApiInfo(data) {
        const version = data["version"];
        const versionToken = '{version}';
        const codeBlocks = document.querySelectorAll('.md-content pre code');
        for(const codeBlock of codeBlocks) {
            codeBlock.innerHTML = codeBlock.innerHTML.replace(new RegExp(versionToken, 'g'), version);
        }
    }
    
    async function fetchApiInfo() {
        const tag = await fetch("https://api.github.com/repos/decentsoftware-eu/DecentHolograms/releases/latest").then(_ => _.json());
        
        const data = {
            "version": tag.tag_name
        };
        
        __md_set("__api_tag", data, sessionStorage);
        loadApiInfo(data);
    }
    
    if(location.href.includes('/api/get-started')) {
        const cachedApi = __md_get("__api_tag", sessionStorage);
        if((cachedApi != null) && (cachedApi["version"])) {
            loadApiInfo(cachedApi);
        } else {
            fetchApiInfo();
        }
    }
})