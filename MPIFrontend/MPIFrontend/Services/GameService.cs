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
    }
}