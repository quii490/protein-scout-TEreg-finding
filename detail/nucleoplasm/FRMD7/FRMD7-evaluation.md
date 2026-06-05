---
type: protein-evaluation
gene: "FRMD7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FRMD7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FRMD7 |
| 蛋白名称 | FERM domain-containing protein 7 |
| 蛋白大小 | 714 aa / 81.6 kDa |
| UniProt ID | Q6ZUT3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm, Cytosol; UniProt: Cell projection, neuron projection; Cell projection, growth  |
| 蛋白大小 | 10/10 | ×1 | 10 | 714 aa / 81.6 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=89 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019749, IPR014847, IPR041788, IPR014352, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Cell projection, neuron projection; Cell projection, growth cone | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- growth cone (GO:0030426)
- neuron projection (GO:0043005)
- neuronal cell body (GO:0043025)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 89 |
| PubMed broad count | 113 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FRMD7-Related Infantile Nystagmus.. **. PMID: 20301748
2. Nystagmus in childhood.. *Pediatrics and neonatology*. PMID: 25086850
3. Correlations of FRMD7 gene mutations with ocular oscillations.. *Scientific reports*. PMID: 35705619
4. Expression and localization of FRMD7 in human fetal brain, and a role for F-actin.. *Molecular vision*. PMID: 21386928
5. FRMD7 Gene Alterations in a Pakistani Family Associated with Congenital Idiopathic Nystagmus.. *Genes*. PMID: 36833273

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.9 |
| 高置信度残基 (pLDDT>90) 占比 | 36.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 51.1% |
| 有序区域 (pLDDT>70) 占比 | 42.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.9），有序残基占 42.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019749, IPR014847, IPR041788, IPR014352, IPR035963; Pfam: PF08736, PF09380, PF00373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CASK | 0.932 | 0.326 | — |
| GPR143 | 0.925 | 0.000 | — |
| NYX | 0.799 | 0.000 | — |
| OPN1MW | 0.789 | 0.000 | — |
| OPN1LW | 0.767 | 0.000 | — |
| SLC38A8 | 0.645 | 0.000 | — |
| HPS5 | 0.626 | 0.000 | — |
| CDR1 | 0.560 | 0.000 | — |
| SLC25A14 | 0.505 | 0.000 | — |
| CRYBB3 | 0.500 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CLNS1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.9 + PDB: 无 | pLDDT=61.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, neuron projection; Cell projectio / Plasma membrane; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. FRMD7 — FERM domain-containing protein 7，研究基础较多，新颖性有限。
2. 蛋白大小714 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 89 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZUT3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165694-FRMD7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FRMD7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZUT3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000165694-FRMD7/subcellular

![](https://images.proteinatlas.org/886/1969_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/886/1969_F8_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/886/53_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/886/53_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/886/55_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/886/55_G8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZUT3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
