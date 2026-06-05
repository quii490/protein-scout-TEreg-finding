---
type: protein-evaluation
gene: "Ppan"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Ppan 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Ppan / BXDC3, SSF1 |
| 蛋白名称 | Suppressor of SWI4 1 homolog |
| 蛋白大小 | 473 aa / 53.2 kDa |
| UniProt ID | Q9NQ55 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 473 aa / 53.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=72.2; PDB: 8FKP, 8FKQ, 8FKR, 8FKS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007109, IPR045112; Pfam: PF04427 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleus (GO:0005634)
- preribosome, large subunit precursor (GO:0030687)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 99 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BXDC3, SSF1 |

**关键文献**:
1. NAT10 triggers colorectal cancer progression via promoting PPAN-regulated DNA damage repair.. *Oncogene*. PMID: 41455833
2. Ppan is essential for preimplantation development in mice†.. *Biology of reproduction*. PMID: 35554497
3. The Wnt Target Protein Peter Pan Defines a Novel p53-independent Nucleolar Stress-Response Pathway.. *The Journal of biological chemistry*. PMID: 25759387
4. Loss of Peter Pan protein is associated with cell cycle defects and apoptotic events.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 30716409
5. Pescadillo homologue 1 and Peter Pan function during Xenopus laevis pronephros development.. *Biology of the cell*. PMID: 21770895

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 23.3% |
| 置信残基 (pLDDT 70-90) 占比 | 38.5% |
| 中等置信 (pLDDT 50-70) 占比 | 17.3% |
| 低置信 (pLDDT<50) 占比 | 20.9% |
| 有序区域 (pLDDT>70) 占比 | 61.8% |
| 可用 PDB 条目 | 8FKP, 8FKQ, 8FKR, 8FKS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8FKP, 8FKQ, 8FKR, 8FKS）+ AlphaFold高质量预测（pLDDT=72.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007109, IPR045112; Pfam: PF04427 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000253107.7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LYAR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SMNDC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| VP24 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| TAF1D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SMAD2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23764002|imex:IM-20916 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 8FKP, 8FKQ, 8FKR, 8FKS | pLDDT=72.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. Ppan — Suppressor of SWI4 1 homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小473 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ55
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130810-PPAN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Ppan
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ55
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQ55-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
