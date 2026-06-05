---
type: protein-evaluation
gene: "NSMCE4A"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NSMCE4A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NSMCE4A / C10orf86 |
| 蛋白名称 | Non-structural maintenance of chromosomes element 4 homolog A |
| 蛋白大小 | 385 aa / 44.3 kDa |
| UniProt ID | Q9NXX6 |
| 评估日期 | 2026-06-04 |

**功能简介** (UniProt): Component of the SMC5-SMC6 complex, a complex involved in DNA double-strand breaks by homologous recombination. The complex may promote sister chromatid homologous recombination by recruiting the SMC1-SMC3 cohesin complex to double-strand breaks. The complex is required for telomere maintenance via recombination in ALT (alternative lengthening of telomeres) cell lines and mediates sumoylation of s...

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, telomere |
| 蛋白大小 | 10/10 | ×1 | 10 | 385 aa / 44.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027786, IPR014854, IPR029225; Pfam: PF15412, PF |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **153.0/180** | |
| **归一化总分** | | | **85.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome, telomere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- Smc5-Smc6 complex (GO:0030915)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf86 |

**关键文献**:
1. Proteomic Analysis of Human Topoisomerases Reveals Their Distinct and Diverse Cellular Functions.. *Molecular & cellular proteomics : MCP*. PMID: 41043513
2. Positive Selection Drives the Evolution of the Structural Maintenance of Chromosomes (SMC) Complexes.. *Genes*. PMID: 39336750
3. Developing diagnostic biomarkers for Alzheimer's disease based on histone lactylation-related gene.. *Heliyon*. PMID: 39315143
4. Interaction between NSMCE4A and GPS1 links the SMC5/6 complex to the COP9 signalosome.. *BMC molecular and cell biology*. PMID: 32384871
5. [Bioinformatics analysis and construction of eukaryotic expression vector of MAGE-D4].. *Xi bao yu fen zi mian yi xue za zhi = Chinese journal of cellular and molecular immunology*. PMID: 33148382

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.9 |
| 高置信度残基 (pLDDT>90) 占比 | 23.9% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 19.0% |
| 低置信 (pLDDT<50) 占比 | 26.5% |
| 有序区域 (pLDDT>70) 占比 | 54.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.9），有序残基占 54.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027786, IPR014854, IPR029225; Pfam: PF15412, PF08743 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NSMCE1 | 0.999 | 0.972 | — |
| SMC6 | 0.999 | 0.974 | — |
| SMC5 | 0.999 | 0.972 | — |
| NSMCE3 | 0.998 | 0.908 | — |
| NSMCE2 | 0.995 | 0.815 | — |
| SUMO4 | 0.922 | 0.092 | — |
| EID3 | 0.907 | 0.000 | — |
| SLF2 | 0.866 | 0.589 | — |
| SLF1 | 0.835 | 0.451 | — |
| ZNF597 | 0.828 | 0.828 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 6 / 15 = 40%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 40%，PPI数据支持功能研究。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.9 + PDB: 无 | pLDDT=69.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, telomere / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NSMCE4A — Non-structural maintenance of chromosomes element 4 homolog A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小385 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXX6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107672-NSMCE4A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NSMCE4A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXX6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live via harvest pipeline; evaluated 2026-06-04

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000107672-NSMCE4A/subcellular

![](https://images.proteinatlas.org/37459/517_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/37459/517_E5_4_red_green.jpg)
![](https://images.proteinatlas.org/37459/520_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/37459/520_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/37459/523_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/37459/523_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
