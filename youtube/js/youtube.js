var channelName = 'frickyfreshboy';
var vidWidth = '500';
var vidHeight = '400';

$(document).ready(function(){
	$.get(
	"https://www.googleapis.com/youtube/v3/channels",{
		part: 'contentDetails',
		forUsername: channelName,
		key: 'AIzaSyBhJZ6lKKc8sYgnxz4_7Nm2a56Wu1_kETA'},
		function(data){
			$.each(data.items, function(i, item){
				console.log(item);
				pid = item.contentDetails.relatedPlaylists.uploads;
				getVids(pid);
			})

		}

	);

function getVids(pid){
	$.get(
	"https://www.googleapis.com/youtube/v3/playlistItems",{
		part: 'snippet',
		maxResults: 5,
		playlistId: pid,
		key: 'AIzaSyBhJZ6lKKc8sYgnxz4_7Nm2a56Wu1_kETA'},
		function(data){
			var output;
			$.each(data.items, function(i, item){
				console.log(item);
				videTitle = item.snippet.title;
				videoId = item.snippet.resourceId.videoId;

				output = '<li><iframe height"" width="" src=\"//www.youtube.com/embed/'+videoId+'\"></iframe></li>';

				//append to results listStyleType
				$('#results').append(output);

			})

		}

	);
	}
});