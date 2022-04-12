/** Coding excrcises written for the position
  * of https://jobs.amd.com/job/Austin-Software-Development-Engineer-1-Texa/853677600/
  * author: Tianwen Su
  */ 

/** task 1, JSON processing.
  * @param rankings: an array of dictionary.
  * @return: a dictionary contains key top2, 
  * which value is an array of strings.
  */
function topTwoRankedProduct(rankings)
{
    var var_ranking = rankings;
    // sorted by rank in increasing order.
    var_ranking.sort((a, b) => a.rank-b.rank);

    // pick the first 2 elements.
    var top_2 = var_ranking.slice(0, Math.min(2, var_ranking.length));
    return {'top2': 
        top_2.map(e => e.name)
    };
}



/** task 2, print out each column of a 2d array
  * in a declarative way.
  * @param data: a 2d array.
  */
function transform(data)
{
    // length of column.
    let n = Math.max(...data.map(r => r.length));
    // [0, ..., n-1]
    let range = [...Array(n).keys()];
    // for 0 <= i < n, print an array contains ith element
    // of each row in data.
    range.forEach(i =>
        console.log(data.map(row => row[i]))
    );
}
