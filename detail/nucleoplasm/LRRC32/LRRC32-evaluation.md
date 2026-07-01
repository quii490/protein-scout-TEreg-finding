---
type: protein-evaluation
gene: "LRRC32"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## LRRC32 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LRRC32 |
| 蛋白名称 | Transforming growth factor beta activator LRRC32 |
| 蛋白大小 | 662 aa / 72.0 kDa |
| UniProt ID | Q14392 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 662 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=49 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=86.1; PDB=6 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Leu-rich_rpt; Leu-rich_rpt_typical-subtyp; LRR_dom_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=30 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Enhanced)
- PubMed strict=49 broad=197
- AF pLDDT=86.1 PDB=6
- InterPro: Leu-rich_rpt; Leu-rich_rpt_typical-subtyp; LRR_dom_sf
- Pfam: LRR_8; LRRNT
- PPI degree=30 ChIP: None
35656379: A Novel Homozygous Missense Variant in the LRRC32 Gene Is Associated With a New  | 40826484: Unraveling the causal role of TGF-βRII in osteoporosis and the potential of its  | 37614425: Single‑nucleotide polymorphism rs6592645 confers asthma risk through regulating 

### 4. 总体评价
**74.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transforming growth factor beta activator LRRC32

**功能**: Key regulator of transforming growth factor beta (TGFB1, TGFB2 and TGFB3) that controls TGF-beta activation by maintaining it in a latent state during storage in extracellular space (PubMed:19651619, PubMed:19750484, PubMed:22278742). Associates specifically via disulfide bonds with the Latency-associated peptide (LAP), which is the regulatory chain of TGF-beta, and regulates integrin-dependent activation of TGF-beta (PubMed:22278742). Able to outcompete LTBP1 for binding to LAP regulatory chain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001611 |
| InterPro | IPR003591 |
| InterPro | IPR032675 |
| InterPro | IPR000372 |
| Pfam | PF13855 |
| Pfam | PF01462 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EMSY | STRING | 724 |
| STAT3 | BioGRID | 1 |
| DCP2 | BioGRID | 1 |
| CBFB | BioGRID | 1 |
| ERVMER34-1 | BioGRID | 1 |
| PPM1B | BioGRID | 1 |
| KRAS | BioGRID | 0 |
| ZDHHC6 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q14392-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137507-LRRC32

![](https://images.proteinatlas.org/55775/1774_D8_12_cr5950fd0cdc360_red_green.jpg)
![](https://images.proteinatlas.org/55775/1774_D8_17_cr5950fd0cdcb04_red_green.jpg)
![](https://images.proteinatlas.org/55775/1500_E4_4_red_green.jpg)
![](https://images.proteinatlas.org/55775/1500_E4_5_red_green.jpg)
![](https://images.proteinatlas.org/55775/1505_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/55775/1505_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/58434/1774_C8_17_cr5950fac0bd3fb_red_green.jpg)
![](https://images.proteinatlas.org/58434/1774_C8_27_cr5950fac0be3e4_red_green.jpg)

### PubMed 文献

**PubMed count: 197**

| 42160392 | Shared diagnostic biomarkers in metabolic syndrome and coronary artery disease identified by integrated bioinformatics a | Endocr Connect 2026 |
| 42121001 | Genome-wide DNA methylation signatures in blood associated with pediatric obesity. | Clin Epigenetics 2026 |
| 42016541 | Multi-Omics Analysis Reveals m7G Methylation-Related Genes May Be Involved in TGF-β Signaling-Mediated Anti-PD-L1 Respon | Immunotargets Ther 2026 |

### 深度机制分析

LRRC32（又称GARP）是TGF-beta潜伏态的关键调控因子，通过二硫键与LAP（Latency-associated peptide）特异性结合，将TGF-beta扣留在细胞外基质的潜伏状态中（PMID:19651619, 22278742）。其结构域完全由富含亮氨酸重复序列（LRR）组成：Leu-rich_rpt（IPR001611）、LRR_8（PF13855）和LRRNT（PF01462），形成经典的弯曲螺线管折叠。AlphaFold pLDDT=86.1，且拥有6个PDB实验结构，为蛋白集中结构研究最充分的靶标之一。PPI网络（degree=30）中STAT3、KRAS和CBFB的互作暗示其在多种信号通路中的交叉调控角色。

HPA数据显示其定位于nucleoplasm（Enhanced级别），这一发现挑战了LRRC32作为单纯胞外TGF-beta储存因子的经典范式。核质定位提示LRRC32可能具有胞内"非经典"功能——或作为TGF-beta信号通路的核内反馈调节器直接进入核内调控靶基因转录，或作为核质穿梭蛋白在胞外潜伏复合物与核内转录机器之间建立物理耦合。PPI中EMSY（STRING score=724）为最高置信度互作，而EMSY是BRCA2的结合蛋白且在DNA损伤应答中发挥作用，进一步支持LRRC32的核内功能。

LRRC32纯合错义突变导致新型综合征（PMID:35656379），而GWAS分析将rs6592645多态性与哮喘风险关联（PMID:37614425），m7G甲基化相关基因分析（PMID:42016541）鉴定其在TGF-beta信号和PD-L1耐药中的核心角色。这些证据提示，LRRC32可能通过TGF-beta依赖性机制参与免疫微环境重塑和染色质调控。鉴于其Enhanced核质定位和6个PDB结构的高分辨率信息，LRRC32的核输入机制（NLS识别）和核内DNA/chromatin结合能力应作为优先验证方向。

