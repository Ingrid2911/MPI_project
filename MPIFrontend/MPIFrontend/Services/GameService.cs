using MPIFrontend.Models;

namespace MPIFrontend.Services
{
    public class GameService
    {
        private readonly IHttpClientFactory _httpClientFactory;

        public GameService(IHttpClientFactory httpClientFactory)
        {
            _httpClientFactory = httpClientFactory;
        }

        public async Task<List<Game>> GetGamesAsync()
        {
            var client = _httpClientFactory.CreateClient("PythonApi");
            return await client.GetFromJsonAsync<List<Game>>("/api/games") ?? new List<Game>();
        }

        public async Task<Game> GetGameAsync(string id)
        {
            var client = _httpClientFactory.CreateClient("PythonApi");
            return await client.GetFromJsonAsync<Game>($"/api/games/{id}") ?? new Game();
        }

        public async Task CreateGameAsync(Game game)
        {
            var client = _httpClientFactory.CreateClient("PythonApi");
            await client.PostAsJsonAsync("/api/games", game);
        }

        public async Task UpdateGameAsync(string id, Game game)
        {
            var client = _httpClientFactory.CreateClient("PythonApi");
            await client.PutAsJsonAsync($"/api/games/{id}", game);
        }

        public async Task DeleteGameAsync(string id)
        {
            var client = _httpClientFactory.CreateClient("PythonApi");
            await client.DeleteAsync($"/api/games/{id}");
        }
    }
}