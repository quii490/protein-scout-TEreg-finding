---
type: protein-evaluation
gene: "ELF5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ELF5 — REJECTED (研究热度过高 (PubMed strict=167，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELF5 / ESE2 |
| 蛋白名称 | ETS-related transcription factor Elf-5 |
| 蛋白大小 | 265 aa / 31.3 kDa |
| UniProt ID | Q9UKW6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 265 aa / 31.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=167 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=70.8; PDB: 1WWX |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 167 |
| PubMed broad count | 259 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ESE2 |

**关键文献**:
1. Single-nucleus chromatin accessibility and transcriptomic map of breast tissues of women of diverse genetic ancestry.. *Nature medicine*. PMID: 39122969
2. ELF5-Mediated AR Activation Regulates Prostate Cancer Progression.. *Scientific reports*. PMID: 28287091
3. Genetic Study of Elf5 and Ehf in the Mouse Salivary Gland.. *Journal of dental research*. PMID: 36348499
4. Breast-Specific Molecular Clocks Comprised of ELF5 Expression and Promoter Methylation Identify Individuals Susceptible to Cancer Initiation.. *Cancer prevention research (Philadelphia, Pa.)*. PMID: 34140348
5. Coordinate regulation of ELF5 and EHF at the chr11p13 CF modifier region.. *Journal of cellular and molecular medicine*. PMID: 31557407

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 34.3% |
| 置信残基 (pLDDT 70-90) 占比 | 26.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 31.3% |
| 有序区域 (pLDDT>70) 占比 | 60.3% |
| 可用 PDB 条目 | 1WWX |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=70.8，有序区 60.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR036388; Pfam: PF00178, PF02198 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WFDC5 | 0.826 | 0.000 | — |
| CDX2 | 0.789 | 0.000 | — |
| GATA3 | 0.756 | 0.000 | — |
| EOMES | 0.747 | 0.000 | — |
| TEAD4 | 0.734 | 0.000 | — |
| ITGB3 | 0.669 | 0.000 | — |
| TFAP2C | 0.620 | 0.000 | — |
| GCM1 | 0.604 | 0.000 | — |
| SIRT6 | 0.599 | 0.594 | — |
| CSN2 | 0.540 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SIRT6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RPS15A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBQLN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| ACTR2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NRIP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GLRX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| QDPR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SS18L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| NFE2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| NFE2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32911434|imex:IM-27648 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 1WWX | pLDDT=70.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ELF5 — ETS-related transcription factor Elf-5，研究基础较多，新颖性有限。
2. 蛋白大小265 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 167 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 167 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKW6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135374-ELF5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELF5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKW6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKW6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
