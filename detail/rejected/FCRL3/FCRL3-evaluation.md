---
type: protein-evaluation
gene: "FCRL3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FCRL3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=149，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCRL3 / FCRH3, IFGP3, IRTA3, SPAP2 |
| 蛋白名称 | Fc receptor-like protein 3 |
| 蛋白大小 | 734 aa / 80.9 kDa |
| UniProt ID | Q96P31 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell projection, microvillus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 734 aa / 80.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=149 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007110, IPR036179, IPR013783, IPR050488, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **63.5/180** | |
| **归一化总分** | | | **35.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell projection, microvillus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- external side of plasma membrane (GO:0009897)
- microvillus membrane (GO:0031528)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 149 |
| PubMed broad count | 217 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FCRH3, IFGP3, IRTA3, SPAP2 |

**关键文献**:
1. Potential drug targets for multiple sclerosis identified through Mendelian randomization analysis.. *Brain : a journal of neurology*. PMID: 36864689
2. An international genome-wide meta-analysis of primary biliary cholangitis: Novel risk loci and candidate drugs.. *Journal of hepatology*. PMID: 34033851
3. Transcriptional and spatial profiling of the kidney allograft unravels a central role for FcyRIII+ innate immune cells in rejection.. *Nature communications*. PMID: 37468466
4. Immunogenetics of IgG4-Related AIP.. *Current topics in microbiology and immunology*. PMID: 27832379
5. FCRL3 gene polymorphisms as risk factors for rheumatoid arthritis.. *Human immunology*. PMID: 26746625

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.2 |
| 高置信度残基 (pLDDT>90) 占比 | 52.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 22.8% |
| 有序区域 (pLDDT>70) 占比 | 73.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.2，有序区 73.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR050488, IPR003599; Pfam: PF00047, PF13895, PF13927 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZAP70 | 0.830 | 0.321 | — |
| PTPN22 | 0.809 | 0.069 | — |
| SYK | 0.800 | 0.321 | — |
| PIGR | 0.757 | 0.067 | — |
| PTPN11 | 0.741 | 0.312 | — |
| MS4A1 | 0.700 | 0.173 | — |
| FCRL1 | 0.660 | 0.000 | — |
| TIGIT | 0.624 | 0.000 | — |
| CD5L | 0.611 | 0.000 | — |
| CTLA4 | 0.591 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AGPAT4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| IGFBP5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CMTM5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SLC2A5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC30A3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MS4A1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STATH | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAP4K3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.2 + PDB: 无 | pLDDT=77.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, microvillus membra / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FCRL3 — Fc receptor-like protein 3，研究基础较多，新颖性有限。
2. 蛋白大小734 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 149 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96P31
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160856-FCRL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCRL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96P31
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
