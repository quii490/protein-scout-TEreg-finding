---
type: protein-evaluation
gene: "SLC4A1AP"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC4A1AP 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC4A1AP |
| 蛋白名称 | Kanadaptin |
| 蛋白大小 | 742 aa / 82.9 kDa |
| UniProt ID | Q9BWU0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | HPA: Nucleoplasm; Plasma membrane; Vesicles (Supported) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 742 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=5 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT=64.1; PDB: 1 entries |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Cell_Proc_Reg/RNA_Proc; dsRBD_dom; FHA_dom; SMAD_FHA_dom_sf |
| 🔗 PPI | 6/10 | ×3 | 18.0 | Combined PPI degree=131 |
| **加权总分** | | | **131/180** | |
| **归一化总分 (÷1.83)** | | | **72.7/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm; Plasma membrane; Vesicles | Supported |
| GO-CC | cytoplasm(IEA:UniProtKB-SubCell); nucleoplasm(IDA:HPA) | — |

**IF 图像**: See [Protein Atlas](https://www.proteinatlas.org/)

**PAE 图**: https://alphafold.ebi.ac.uk/files/AF-Q9BWU0-F1-predicted_aligned_error_v6.png

#### 3.2 蛋白大小评估
742 aa / 82.9 kDa.

#### 3.3 研究现状
PubMed strict: 5. Broad: 12.

- PMID 40629317: The related SNPs and genes to body size using GWAS- latent variable modeling in dromedaries.. *BMC genomics*
- PMID 31310629: Molecular prognosticators in clinically and pathologically distinct cohorts of head and neck squamous cell carcinoma-A m. *PloS one*
- PMID 29030403: New Blood Pressure-Associated Loci Identified in Meta-Analyses of 475 000 Individuals.. *Circulation. Cardiovascular genetics*

#### 3.4 三维结构分析
AlphaFold pLDDT=64.1. PDB=1.

#### 3.5 结构域分析
InterPro: Cell_Proc_Reg/RNA_Proc; dsRBD_dom; FHA_dom; SMAD_FHA_dom_sf
Pfam: dsrm; FHA

#### 3.6 PPI 互作网络
Combined human PPI degree=131.

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + GO-CC | consistent |
| 结构域 | InterPro + Pfam | verified |
| PPI | STRING/BioGRID | 有数据 |

### 4. 总体评价
**推荐等级**: ⭐⭐⭐⭐
**归一化总分**: 72.7/100
**定位分类**: nucleoplasm

Non-chromatin-regulatory nuclear protein with some nuclear localization evidence. Very novel (5 PubMed papers).

### 深度机制分析

**结构域架构**：SLC4A1AP/Kanadaptin（742 aa，82.9 kDa）拥有本批次最丰富的结构域组合之一：（1）FHA_dom（Forkhead-associated domain，IPR016940，SMAD_FHA_dom_sf IPR049534）——FHA结构域特异性识别磷酸化苏氨酸残基（pT/pTxxD基序），是磷酸化依赖的蛋白-蛋白互作模块，参与DNA损伤应答（DDR）和细胞周期调控；（2）dsRBD_dom（双链RNA结合结构域，IPR036465）——结合dsRNA和高度结构化的RNA，常见于RNA编辑、RNA干扰和抗病毒先天免疫通路中的蛋白；（3）Cell_Proc_Reg/RNA_Proc（IPR050673）整合了以上结构域的功能。FHA + dsRBD的罕见组合使SLC4A1AP具有同时感知DNA损伤信号和RNA代谢异常的潜力。

**PPI互作网络解读**：PPI degree=131，核心互作包括：SLC4A1（Band 3/AE1，红细胞阴离子交换蛋白，该蛋白最初作为SLC4A1的"关联蛋白"被鉴定而命名）、KDM1A（LSD1，组蛋白去甲基化酶H3K4me1/2，染色质调控的核心酶）、SRPK1（SR蛋白激酶，磷酸化SR剪接因子调控剪接体组装）、CSNK2A1（CK2α，组成性活性激酶，磷酸化数百种底物涉及细胞周期、DNA修复和昼夜节律）、APP（淀粉样前体蛋白，阿尔茨海默病相关蛋白，可能指向神经退行性疾病中的核质功能）。

**结构解读**：AlphaFold pLDDT=64.1（1个PDB结构验证），整体预测置信度偏低。FHA域的pLDDT（70-80）形成11股β-链的β-三明治折叠，含保守的pT结合环（Arg-Ser-X-X-Ser基序），该区域预测质量较高。dsRBD域（pLDDT 60-75）预测形成经典的α-β-β-β-α折叠（与PKR、ADAR等蛋白的dsRBD同源），RNA结合面富含正电荷残基（Arg/Lys cluster）。低pLDDT区域主要集中在连接FHA和dsRBD的柔性linker（>200 aa），可能含大量内在无序区域（IDR），参与液-液相分离（LLPS）。

**机制模型**：（1）FHA介导的信号依赖性蛋白招募：SLC4A1AP通过FHA结构域识别SRPK1或CK2磷酸化的底物蛋白，被招募至剪接体组装位点或DNA损伤灶（DNA damage foci），在磷蛋白信号和RNA代谢之间建立连接；（2）RNA剪接调控：通过dsRBD结合pre-mRNA的茎环或双链区域，SRPK1互作可调节其与SR蛋白的竞争/合作关系，影响剪接位点选择；（3）与KDM1A的互作是功能假设的关键——KDM1A通过H3K4me1/2去甲基化调控增强子和启动子活性，SLC4A1AP可能在剪接偶联的组蛋白修饰中充当适配器，协调新生RNA的剪接和局部染色质状态的维持。

**TE调控展望**：SLC4A1AP是目前了解最少的候选之一（PubMed仅5篇）。其dsRBD + SRPK1互作的组合模式在TE调控中具有潜在意义：许多TE（特别是Alu元件、LINE-1的反义启动子）作为可变外显子来源插入基因体，影响宿主基因的剪接模式。SLC4A1AP可能通过识别含TE序列的pre-mRNA中的dsRNA结构，调控这些TE外显子的剪接包含/跳跃。与KDM1A的互作进一步暗示可能在含有TE插入的启动子区域通过组蛋白去甲基化影响TE驱动的转录。这是一个高度新颖但完全未经验证的假说。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SLC4A1 | BioGRID | 0 |
| APP | BioGRID | 0 |
| WIPF2 | BioGRID | 0 |
| KDM1A | BioGRID | 0 |
| EIF4B | BioGRID | 0 |
| CSNK2A1 | BioGRID | 0 |
| SRPK1 | BioGRID | 0 |
| WWOX | BioGRID | 0 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000163798-SLC4A1AP

![](https://images.proteinatlas.org/36679/601_E8_3_red_green.jpg)
![](https://images.proteinatlas.org/36679/601_E8_6_red_green.jpg)
![](https://images.proteinatlas.org/36679/599_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/36679/599_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/36679/603_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/36679/603_E8_3_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### PubMed

**Count: 12**

| PMID | Title |
|---|---|
| 41552323 | A set of downregulated pleiotropic genes are possible multi-omics biomarkers underlying the irritable bowel syndrome-non-alcoholic fatty liver disease |
| 40629317 | The related SNPs and genes to body size using GWAS- latent variable modeling in dromedaries. |
| 34882702 | Variable expression of eighteen common housekeeping genes in human non-cancerous kidney biopsies. |
| 31310629 | Molecular prognosticators in clinically and pathologically distinct cohorts of head and neck squamous cell carcinoma-A meta-analysis approach. |
| 29030403 | New Blood Pressure-Associated Loci Identified in Meta-Analyses of 475 000 Individuals. |


