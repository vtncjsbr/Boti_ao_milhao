/**
 * Shared axios instance: base URL, default headers and the bearer token.
 */
const ApiClient = (function () {
    const TOKEN_KEY = "meu_access_token";

    const api = axios.create({
        baseURL: window.API_BASE_URL || "",
        headers: { Accept: "application/json" },
    });

    function getToken() {
        return localStorage.getItem(TOKEN_KEY);
    }

    function setToken(token) {
        if (token) {
            localStorage.setItem(TOKEN_KEY, token);
            api.defaults.headers.common.Authorization = `Bearer ${token}`;
        } else {
            localStorage.removeItem(TOKEN_KEY);
            delete api.defaults.headers.common.Authorization;
        }
    }

    setToken(getToken());

    return { api, getToken, setToken };
})();
