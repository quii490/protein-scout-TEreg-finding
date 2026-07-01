---
type: protein-evaluation
gene: "RGMB"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RGMB 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RGMB |
| 蛋白名称 | Repulsive guidance molecule B |
| 蛋白大小 | 437 aa / 47.5 kDa |
| UniProt ID | Q6NW40 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 437 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=74 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=79.5; PDB=11 |
| 调控结构域 | 4/10 | x2 | 8.0 | RGM; RGM_C; RGM_N |
| PPI | 5/10 | x3 | 15.0 | PPI degree=16 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=74 broad=129
- AF pLDDT=79.5 PDB=11
- InterPro: RGM; RGM_C; RGM_N
- Pfam: RGM_C; RGM_N
- PPI degree=16 ChIP: None
29852497: Necroptosis in Acute Kidney Injury. | 39375839: Repulsive guidance molecules b (RGMb): molecular mechanism, function and role in | 38049831: Proteomic insights into the associations between obesity, lifestyle factors, and

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Repulsive guidance molecule B

**功能**: Member of the repulsive guidance molecule (RGM) family that contributes to the patterning of the developing nervous system (By similarity). Acts as a bone morphogenetic protein (BMP) coreceptor that potentiates BMP signaling (By similarity). Promotes neuronal adhesion (By similarity). May inhibit neurite outgrowth

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR040287 |
| InterPro | IPR009496 |
| InterPro | IPR010536 |
| Pfam | PF06534 |
| Pfam | PF06535 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RGMA | STRING | 909 |
| PRRXL1 | STRING | 878 |
| DRGX | STRING | 878 |
| ERBB2 | BioGRID | 1 |
| EGFR | BioGRID | 1 |
| BMP2 | BioGRID | 0 |
| BMP4 | BioGRID | 0 |
| ACVR1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6NW40-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000174136-RGMB

![](https://images.proteinatlas.org/16993/138_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/16993/138_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/16993/166_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/16993/166_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/16993/139_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/16993/139_D8_2_red_green.jpg)

### 深度机制分析

**结构域架构**：RGMB（437 aa，47.5 kDa）是排斥导向分子B（Repulsive Guidance Molecule B），属于RGM家族的GPIA锚定膜蛋白，采用保守的双结构域组织：RGM_N（IPR010536, PF06535）——N端结构域（约1-160 aa），采用α/β折叠（α/β sandwich），含保守的proteolytic cleavage位点（furin/PC家族蛋白酶的RXRR基序）用于激活性蛋白水解释放功能性配体；RGM_C（IPR009496, PF06534）——C端结构域（约160-420 aa），采用von Willebrand factor type D (VWD) 样折叠，含多个β-片层堆叠形成配体结合平台。AlphaFold pLDDT=79.5，实验PDB=11（本批次中PDB覆盖最多者，结构解析充分）。HPA定位Nucleoplasm（Approved）。

**PPI互作网络解读**：PPI degree=16，互作集中在BMP信号和轴突导向通路：BMP2/BMP4（骨形态发生蛋白，BioGRID 0）——RGMB作为BMP辅助受体（coreceptor），通过RGM_C结构域结合BMP2/4并增强其与I型/II型BMP受体（BMPRI/II）的亲和力和信号特异性；RGMA（STRING 909，家族同源蛋白RGM-A/排斥导向分子A）——异源二聚化或竞争相同的BMP配体；ERBB2/EGFR（BioGRID 1）——非经典互作，提示RGMB可能与生长因子受体存在交叉对话；ACVR1（ALK2, I型BMP受体，BioGRID 0）——RGMB通过同时结合BMP配体和BMP受体来增强BMP信号强度（增强Smad1/5/9磷酸化）。PRRXL1和DRGX（STRING 878）为神经元特异性转录因子，提示RGMB在神经发育中的功能。

**结构解读**：RGM_N采用α/β三明治折叠——中央4条反平行β-链被两侧α-螺旋包围，形成稳定的折叠核心。Furin切割位点（RxxR↓）位于结构域间的柔性linker上，切割后释放N端片段——N端片段可能具有独立功能（如自分泌/旁分泌信号分子）。RGM_C的VWD样折叠包含多个互锁的β-片层形成弯曲的β-棱柱（β-prism），BMP结合面位于β-棱柱的凹面——保守的疏水性残基簇和氢键供体/受体排列形成BMP2/4的受体结合表位（finger/knuckle表位）的互补界面。PDB=11涵盖了RGMB-BMP2复合体、RGMB-Neogenin复合体等多种结构状态。

**机制模型**：（1）经典BMP辅助受体功能——RGMB以两种模式运作：膜锚定模式（GPIA）将BMP配体呈递给相邻细胞的BMP受体（trans signaling），或经furin切割释放可溶性胞外片段作为BMP拮抗剂（cis inhibition by soluble decoy receptor）；（2）Neogenin轴突导向——RGMB通过RGM_C结构域以高亲和力结合Neogenin受体，介导轴突排斥性导向，RGM-Neogenin信号轴与BMP信号独立运作或协同运作（取决于发育环境）；（3）核质定位的潜在机制——RGMB的全长蛋白经GPIA锚定后通常定位于膜脂筏微区（lipid raft），但HPA的Nucleoplasm信号提示可能经蛋白水解释放的胞内片段或未完全修饰的pre-pro-form被核输入装置识别并转运至核质。核内RGMB可能作为BMP信号的核内传感器——已知Smad复合体（BMP信号的转录效应器）在核内靶向特定基因组位点，RGMB可能作为Smad辅助因子增强BMP靶基因的转录。

**TE调控展望**：RGMB通过BMP-Smad信号间接连接TE调控。BMP激活的Smad1/5/9复合体与Smad4形成三聚体并靶向含GC-rich/BRE（BMP响应元件，GGCGCC/GCCG序列）的启动子——已知多种LTR/ERV元件含BRE样序列，BMP-Smad可驱动这些LTR的转录。RGMB作为BMP辅助受体决定了BMP信号的强度阈值和持续时间，因此可能影响BMP-Smad-TE转录轴的输出水平。此外，RGMB通过ERBB2/EGFR互作可能与Ras-MAPK通路交叉——MAPK信号与Smad的cross-talk（如Erk磷酸化Smad1 linker区抑制其核转位）是已知的TE转录调控模式。PMID:38049831的蛋白组学分析将RGMB与肥胖代谢表型关联，侧面揭示了其功能广度。

### PubMed 文献

**PubMed count: 129**

| 41903524 | Graded BMP signals modulate yellow and red color in fishes, impacting adult pigment patterns and conspecific shoaling be | Curr Biol 2026 |
| 41874668 | A Large-Scale Multi-omics Polygenic Risk Score Analysis Identified Candidate Biomarkers Associated with Heel Bone Minera | Calcif Tissue Int 2026 |
| 41534828 | Matriptase-2-mediated suppression of hepatic hepcidin expression in mice requires hepatocyte neogenin. | J Biol Chem 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RGMB

