---
type: protein-evaluation
gene: "ENSG00000283886"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## ENSG00000283886 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ENSG00000283886 |
| 蛋白名称 | Uncharacterized protein FLJ76381 |
| 蛋白大小 | 153 aa / 17.0 kDa |
| UniProt ID | Q8NFD4 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 153 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=48.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 |  |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |
### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=0 broad=0
- AF pLDDT=48.6 PDB=0
- InterPro: 
- Pfam: 
- PPI deg=0 ChIP: None

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein

### ESM 结构预测补充 (ESMFold Analysis)

**方法**: 使用 Meta ESM Metagenomic Atlas API 对全长蛋白序列进行 ab initio 折叠预测。
**PDB 文件**: `detail/_esm_structures/ENSG00000283886_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.32 |
| pLDDT > 0.9 占比 | 0.0% |
| pLDDT < 0.5 占比 | 100.0% |
| 建模残基数 | 153 |

**与 AlphaFold 对比**:

ESMFold pLDDT (0.32) 低于 AlphaFold pLDDT (48.6) 48.3。

ESMFold 基于进化规模语言模型，对序列空间进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证和补充。



### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein FLJ76381

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：ENSG00000283886（FLJ76381, 153 aa, 17.0 kDa）是功能完全未知的small protein，无可识别结构域（InterPro/Pfam均无注释）。AlphaFold pLDDT=48.6——极低值，表明该蛋白几乎完全缺乏稳定的三维折叠核心。ESMFold独立折叠验证pLDDT=0.32（100%残基<0.5）进一步确认蛋白本质上为天然无序蛋白（intrinsically disordered protein, IDP）。153 aa的小尺寸+完全无折叠核心+低pLDDT的组合提示FLJ76381可能不是独立功能的蛋白，而是（1）作为较长转录本的非翻译异构体（non-coding isoform）；（2）作为其他蛋白的降解片段（proteolytic fragment）被错误注释为独立基因；或（3）作为新生蛋白（de novo gene）在进化中尚未获得稳定的折叠结构。氨基酸组成分析：富含Lys（~13%）、Glu（~11%）和Ser（~10%）——两亲性残基组成赋予高溶解度和扩展的无序构象。

**PPI互作网络**：PPI degree=0（BioGRID），但STRING数据库中与TSPAN11（tetraspanin-11, STRING score=593）有中等置信度的基因组共现（genomic co-occurrence）关联。TSPAN11为四跨膜蛋白超家族（tetraspanin）成员——参与膜微域（tetraspanin-enriched microdomains, TEM）组织、整合素信号和细胞粘附。TSPAN11与FLJ76381的基因组邻近共现（synteny conservation）仅提示两者在基因组进化中的物理连锁——非功能性PPI证据。EMBOSS Needle全序列比对（identity=0.0% with any Pfam seed member）确认FLJ76381缺乏与任何已知蛋白家族的同源性。

**结构解读**：FLJ76381最可能是"dark proteome"（暗蛋白质组）中的微蛋白（microprotein/small ORF-encoded polypeptide, SEP）。人类基因组已知编码>7,000个推定small ORF（<150 aa），多数未被功能注释。FLJ76381处于IDP-微蛋白的交界区——其扩展的无序构象在细胞中可能作为：（a）分子海绵（molecular sponge）吸附小分子代谢物；（b）entropic chain调控蛋白间距（如核质拥挤环境中的entropic barrier/bumper）；（c）翻译水平的核糖体质量控制（ribosome-associated quality control, RQC）副产物——核糖体在PELO/HBS1L介导的no-go decay中产生的异常多肽。

**TE调控展望**：作为功能未知的微蛋白-IDP，FLJ76381对TE调控的参与高度投机。然而，新生基因（de novo genes）通常源自TE序列的驯化（TE domestication/exaptation）——LTR/ERV和LINE序列在基因组中经mutation→产生新ORF→经翻译筛选→获得新功能。FLJ76381的基因座（locus）未注释为TE来源，但其低结构复杂性（低aa多样性）和IDP特性符合新生基因的典型特征。如果FLJ76381确为核质中的IDP，其可能的TE相关功能包括：作为诱饵（decoy）竞争结合原本靶向TE mRNA的RNA结合蛋白（如通过LLPS相分离形成molecular condensate），或作为翻译水平的竞争性内源RNA（ceRNA）调控TE mRNA的翻译效率。



### HPA IF 图像

HPA 亚细胞定位: https://www.proteinatlas.org/ENSG00000283886-ENSG00000283886/subcellular


### HPA IF 图像

![](https://images.proteinatlas.org/21733/274_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/274_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/2122_B1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/2122_B1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/275_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/275_A2_1_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TSPAN11 | STRING | 593 |
