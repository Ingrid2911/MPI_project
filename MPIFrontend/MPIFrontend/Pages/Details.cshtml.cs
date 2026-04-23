using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using MPIFrontend.Models;
using MPIFrontend.Services;

namespace MPIFrontend.Pages
{
    public class DetailsModel : PageModel
    {
        private readonly GameService _gameService;
        public Game Game { get; set; } = new Game();

        public DetailsModel(GameService gameService)
        {
            _gameService = gameService;
        }

        public async Task<IActionResult> OnGetAsync(string id)
        {
            Game = await _gameService.GetGameAsync(id);
            if (Game == null) return NotFound();
            return Page();
        }

        public async Task<IActionResult> OnPostAsync(string id)
        {
            await _gameService.DeleteGameAsync(id);
            return RedirectToPage("/Index");
        }
    }
}