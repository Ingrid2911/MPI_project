using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using MPIFrontend.Models;
using MPIFrontend.Services;

namespace MPIFrontend.Pages
{
    public class EditGameModel : PageModel
    {
        private readonly GameService _gameService;

        [BindProperty]
        public Game Game { get; set; } = new Game();

        public EditGameModel(GameService gameService)
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
            if (!ModelState.IsValid) return Page();
            await _gameService.UpdateGameAsync(id, Game);
            return RedirectToPage("/Details", new { id });
        }
    }
}