using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using MPIFrontend.Models;
using MPIFrontend.Services;

namespace MPIFrontend.Pages
{
    public class AddGameModel : PageModel
    {
        private readonly GameService _gameService;

        [BindProperty]
        public Game Game { get; set; } = new Game();

        public AddGameModel(GameService gameService)
        {
            _gameService = gameService;
        }

        public void OnGet() { }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                foreach (var error in ModelState.Values.SelectMany(v => v.Errors))
                {
                    Console.WriteLine(error.ErrorMessage);
                }
                return Page();
            }
            await _gameService.CreateGameAsync(Game);
            return RedirectToPage("/Index");
        }
    }
}