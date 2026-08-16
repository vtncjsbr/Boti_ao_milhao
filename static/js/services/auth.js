/**
 * Authentication: login, refresh and logout.
 */
const Auth = (function () {
    const REFRESH_TOKEN_KEY = "meu_refresh_token";
    const { api, setToken } = ApiClient;

    async function login(username, password) {
        const { data } = await api.post(
            "/auth/login_form",
            new URLSearchParams({ username, password })
        );

        setToken(data.access_token);
        localStorage.setItem(REFRESH_TOKEN_KEY, data.refresh_token);
        return data;
    }

    async function refresh() {
        const { data } = await api.get("/auth/refresh", {
            headers: {
                Authorization: `Bearer ${localStorage.getItem(REFRESH_TOKEN_KEY)}`,
            },
        });

        setToken(data.access_token);
        return data;
    }

    function logout() {
        setToken(null);
        localStorage.removeItem(REFRESH_TOKEN_KEY);
        window.location.href = "/login.html";
    }

    return { login, refresh, logout };
})();
