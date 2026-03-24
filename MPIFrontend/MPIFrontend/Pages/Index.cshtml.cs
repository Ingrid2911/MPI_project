using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using MPIFrontend.Models;
using MPIFrontend.Services;

namespace MPIFrontend.Pages
{
    public class IndexModel : PageModel
    {
        private readonly GameService _gameService;
        public List<Game> Games { get; set; } = new List<Game>();

        public IndexModel(GameService gameService)
        {
            _gameService = gameService;
        }

        public async Task OnGetAsync()
        {
            Games = await _gameService.GetGamesAsync();
        }
    }
}
