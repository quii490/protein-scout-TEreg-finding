---
type: protein-evaluation
gene: "SUN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SUN1 — REJECTED (研究热度过高 (PubMed strict=209，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUN1 / KIAA0810, UNC84A |
| 蛋白名称 | SUN domain-containing protein 1 |
| 蛋白大小 | 785 aa / 87.1 kDa |
| UniProt ID | O94901 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Nucleus inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 785 aa / 87.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=209 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.4; PDB: 6R15, 6R16, 6R2I, 7E34, 7Z8Y, 8AU0, 8B46 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045119, IPR032680, IPR040994, IPR012919; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Enhanced |
| UniProt | Nucleus inner membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- meiotic nuclear membrane microtubule tethering complex (GO:0034993)
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 209 |
| PubMed broad count | 420 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0810, UNC84A |

**关键文献**:
1. SUN1/2 controls macrophage polarization via modulating nuclear size and stiffness.. *Nature communications*. PMID: 37828059
2. Lamin A/C deficiency-mediated ROS elevation contributes to pathogenic phenotypes of dilated cardiomyopathy in iPSC model.. *Nature communications*. PMID: 39143095
3. Emery-Dreifuss Muscular Dystrophy.. **. PMID: 20301609
4. Nesprin-2 is a novel scaffold protein for telethonin and FHL-2 in the cardiomyocyte sarcomere.. *The Journal of biological chemistry*. PMID: 38569934
5. A dual-reporter mouse for therapeutic discovery in Angelman syndrome.. *JCI insight*. PMID: 41632831

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.4 |
| 高置信度残基 (pLDDT>90) 占比 | 18.0% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 20.9% |
| 低置信 (pLDDT<50) 占比 | 36.8% |
| 有序区域 (pLDDT>70) 占比 | 42.3% |
| 可用 PDB 条目 | 6R15, 6R16, 6R2I, 7E34, 7Z8Y, 8AU0, 8B46, 8B5X |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.4），有序残基占 42.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045119, IPR032680, IPR040994, IPR012919; Pfam: PF18580, PF09387, PF07738 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC155 | 0.999 | 0.901 | — |
| SYNE2 | 0.999 | 0.452 | — |
| SYNE1 | 0.999 | 0.942 | — |
| EMD | 0.998 | 0.331 | — |
| LMNA | 0.997 | 0.564 | — |
| SUN2 | 0.996 | 0.000 | — |
| SYNE4 | 0.989 | 0.900 | — |
| SYNE3 | 0.984 | 0.124 | — |
| LMNB1 | 0.982 | 0.221 | — |
| TERB1 | 0.969 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000384015.1 | psi-mi:"MI:0404"(comigration in non denaturing gel | pubmed:22632968|imex:IM-17371 |
| RPT1 | psi-mi:"MI:0091"(chromatography technology) | pubmed:11742986|imex:IM-27291 |
| BLM10 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| UBP6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPN6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ACC1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| SCS2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPN9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPN7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| URA7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.4 + PDB: 6R15, 6R16, 6R2I, 7E34, 7Z8Y,  | pLDDT=60.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus inner membrane / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SUN1 — SUN domain-containing protein 1，研究基础较多，新颖性有限。
2. 蛋白大小785 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 209 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 209 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94901
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164828-SUN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94901
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
