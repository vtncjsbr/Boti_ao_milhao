/**
 * Protected report downloads.
 */
const Report = (function () {
    const { api } = ApiClient;

    async function download(endpoint, filename) {
        const { data } = await api.get(endpoint, { responseType: "blob" });

        const url = window.URL.createObjectURL(data);
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", filename);
        document.body.appendChild(link);
        link.click();
        link.parentNode.removeChild(link);
        window.URL.revokeObjectURL(url);
    }

    return { download };
})();
