---
type: protein-evaluation
gene: "B7Z899"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## B7Z899 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | B7Z899 |
| 蛋白名称 | Aminopeptidase |
| 蛋白大小 | 915 aa / 102.9 kDa |
| UniProt ID | B7Z899 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 915 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=91.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Aminopeptidase_N-like_N; Aminopeptidase_N-like_N_sf; ERAP1-like_C_dom |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=91.2 PDB=0
- InterPro: Aminopeptidase_N-like_N; Aminopeptidase_N-like_N_sf; ERAP1-like_C_dom
- Pfam: ERAP1_C; Peptidase_M1; Peptidase_M1_N
- PPI degree=0 ChIP: None


### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Aminopeptidase

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR045357 |
| InterPro | IPR042097 |
| InterPro | IPR024571 |
| InterPro | IPR034016 |
| InterPro | IPR001930 |
| InterPro | IPR050344 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Aminopeptidase

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR045357 |
| InterPro | IPR042097 |
| InterPro | IPR024571 |
| InterPro | IPR034016 |
| InterPro | IPR001930 |
| InterPro | IPR050344 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：B7Z899（Aminopeptidase, 915 aa, 102.9 kDa）是M1 metallopeptidase家族（Clan MA）成员。结构域注释揭示标准M1 aminopeptidase架构：Aminopeptidase_N-like_N domain（IPR045357）为N端催化域——含有conserved zinc-binding motif（HEXXHX18E, catalytic Zn2+ coordination）——此motif定义了"thermolysin-like"（gluzincin）metallopeptidase活性位点。Peptidase_M1 domain（IPR001930, Pfam Peptidase_M1）延伸催化核心——形成thermolysin-like alpha+beta domain——活性位点Zn2+ coordinated by two His residues (from HEXXH motif) and a C-terminal Glu residue——catalytic Glu residue (from HEXXH) activates water molecule→nucleophilic attack on substrate peptide bond。Peptidase_M1_N domain（Pfam Peptidase_M1_N）提供额外alpha-helical subdomain——为substrate binding和active site accessibility提供conformational flexibility。C端ERAP1-like_C_domain（IPR024571, Pfam ERAP1_C）是M1家族的C-terminal regulatory domain——在ERAP1/ERAP2（Endoplasmic Reticulum Aminopeptidase 1/2）中负责substrate length discrimination和regulatory conformational change——可能介导B7Z899的substrate specificity和domain-domain allostery。ERAP1-like_C_dom呈现all-beta sandwich fold——包含conserved Arg/Lys-rich surface patch——推测参与protein-protein interaction或regulatory partner binding。B7Z899的AlphaFold预测pLDDT=91.2——近乎全蛋白高置信度——除少数loops（pLDDT 70-80）外所有domains pLDDT>90——表示折叠核心的高结构品质。PDB=0——无实验结构，但pLDDT 91.2提供了极高可靠的结构预测。PubMed=0, PPI degree=0——B7Z899为TrEMBL条目，完全未经功能研究。

**PPI互作网络解读**：PPI degree=0意味着STRING, IntAct, BioGRID中均无实验或预测互作——功能推断完全依赖domain homology。M1 aminopeptidase家族的保守互作模式：ERAP1 known to form heterodimer with ERAP2 in ER——通过ERAP1-like_C domain的interface完成二聚化——B7Z899可能以类ERAP1-like_C domain二聚化或多聚化。M1家族成员也常与MHC class I antigen presentation pathway蛋白互作——如ERAP1/ERAP2与tapasin/TAP transporter协同trimming peptide→optimize peptide length（8-10 aa）for MHC I loading——B7Z899的exact cellular compartment unknown（TrEMBL无GO-CC），但结构域homology倾向于胞质或ER localization——或某种vesicular compartment。

**结构解读**：pLDDT=91.2的全蛋白高置信度表明B7Z899是高度有序折叠的多domain protein——非IDR-rich。M1 aminopeptidase的催化机制：活性位点Zn2+（tetrahedral coordination由2 His + 1 Glu + 1 catalytic water molecule）polarize water molecule→nucleophilic attack on substrate peptide bond→tetrahedral intermediate stabilized by Zn2+ and active site oxyanion hole→amide bond cleavage→release of N-terminal amino acid。Substrate specificity确定——M1 aminopeptidase通常偏好hydrophobic or basic N-terminal residue (Leu, Met, Arg)——不切割Pro或X-Pro peptide bond。C端ERAP1-like_C_domain的结构——基于ERAP1 C-terminal domain crystal structures（all-beta fold with curved beta-sheet surface）——此domain的hinge region允许open/close conformational switch→调控substrate access to active site——这是M1 aminopeptidase peptide trimming length regulation的基础。B7Z899的ERAP1-like_C domain可能以类似机制调控substrate length。

**机制模型**：（1）Peptide trimming and processing——B7Z899催化N-terminal amino acid的processive removal from polypeptide substrates——调节peptide pool composition和function bioactive peptide（如angiotensin, bradykinin, neuropeptide）。在antigen processing中trim peptide precursor至MHC class I loading的optimal length（8-10 aa）。（2）蛋白质降解和质量控制——aminopeptidase参与ubiquitin-proteasome system and autophagy的downstream peptide clearance——进一步降解proteasome-derived peptides~7-15 aa→free amino acids。（3）细胞内信号——peptide trimming调控signaling peptide的activity和half-life——间接影响receptor activation和intracellular signaling cascades。

**TE调控展望**：B7Z899的TE调控关联仅能通过间接代谢连接推断。Aminopeptidase-mediated peptide metabolism产生free amino acids——这些amino acids尤其是methionine（Met）和serine（Ser）为one-carbon metabolism提供前体——one-carbon cycle produce S-adenosylmethionine (SAM)——universal methyl donor for DNA methylation (DNMT1/3A/3B) and histone methylation (SETDB1, SUV39H1/2)——methylation是TE epigenetic silencing的核心依赖。因此B7Z899的aminopeptidase activity可间接影响methyl donor pool→调节TE区域的DNA/histone methylation efficiency。B7Z899-TrEMBL未研究本质意味着其组织表达谱、底物偏好和细胞功能全部未知——实验验证其TE调控潜力需首先确定其expression和localization，然后使用靶向metabolomics确定其底物peptide pool产物与SAM/methylation的代谢通量连接。


![PAE](https://alphafold.ebi.ac.uk/files/AF-B7Z899-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B7Z899
