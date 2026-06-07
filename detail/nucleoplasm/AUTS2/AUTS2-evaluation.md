---
type: protein-evaluation
gene: "AUTS2"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation, PRC1, neurodevelopment]
status: scored
---

## AUTS2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AUTS2 / KIAA0442 |
| 蛋白大小 | 1259 aa / 139.0 kDa |
| UniProt ID | Q8WXX7 (AUTS2_HUMAN, Swiss-Prot reviewed) |
| Ensembl Gene ID | ENSG00000158321 |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×3 | 21.0 | 核质+胞质双重定位; Protein Atlas: 核质(主)+胞质; UniProt: Nucleus + Cytoplasm/cytoskeleton + Growth cone |
| 📏 蛋白大小 | 5/10 | ×2 | 10.0 | 1259 aa, 139 kDa — 偏大, 生化和结构研究难度高 |
| 🆕 研究新颖性 | 5/10 | ×3 | 15.0 | PubMed 220篇, 以神经发育为主, PRC1-chromatin 角度有一定空间 |
| 🏗️ 三维结构 | 2/10 | ×3 | 6.0 | 平均pLDDT 41.5, 89%无序, 几乎无折叠域 |
| 🧬 调控结构域 | 3/10 | ×2 | 6.0 | 仅AUTS2家族域, 无经典染色质/DNA结合域, >200篇仍无注释域 |
| 🔗 PPI | 2/10 | ×3 | **6** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | +1.0 | 定位2源互证+0.5; 进化保守+0.5 |
| **原始总分** | | | **79.0/158** |
| **归一化总分** | | | **50.0/100** |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | 核质 (Nucleoplasm) + 胞质、质膜、细胞连接 | Supported (核质), Uncertain (其他) |
| GeneCards | Region:Disordered(1-21); Region:Disordered(51-237); Region:Disordered(499-755); Region:Disordered(847-874); Region:Disordered(945-987) | — |
| UniProt | Nucleus + Cytoplasm/cytoskeleton + Growth cone | ECO:0000269 (PubMed) |
| GO | Nucleus, PRC1 complex | IDA |

**Protein Atlas IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/AUTS2/IF_images/U2OS_1.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/AUTS2/IF_images/U2OS_2.jpg]]

**结论**: AUTS2 在核质和胞质均有分布。在核内作为 PRC1-like 复合体组分参与转录调控，在胞质中调控肌动蛋白细胞骨架和神经突生长。这种双重定位限制了其作为纯粹核蛋白的研究价值。得分 7/10。

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 1259 aa / 139 kDa 属于偏大蛋白（1200-2000 aa范围）。全长重组表达困难，不利于常规生化实验（需截短体策略）。但存在多个亚型（最短 ~680 aa），可能适合结构研究。得分 5/10。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 (Title/Abstract) | 220 |
| 最早发表年份 | ~2002 |
| PRC1/Chromatin 相关比例 | ~15-20%（多数为神经发育/自闭症方向） |

**主要研究方向**:
- AUTS2 相关综合征（智力障碍、自闭症谱系障碍）
- 神经元分化和迁移调控（胞质功能）
- PRC1-like 复合体组分（核内功能，2015年发现）
- 与 PCGF5/RNF2 形成非经典 PRC1 复合体调控转录激活

**评价**: 220 篇论文处于中等热度，研究以神经发育为主。PRC1-chromatin 角度在 2015 年才被发现，有一定 niche 空间但整体已被较多关注。得分 5/10。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 41.5 |
| PDB 实验结构 | — |
| pLDDT >90 (高置信度) 占比 | 0.4% (5/1259) |
| pLDDT 70-90 (可信) 占比 | 3.3% (41/1259) |
| pLDDT 50-70 (低置信度) 占比 | 7.7% (97/1259) |
| pLDDT <50 (极低) 占比 | 88.6% (1116/1259) |
| 有序区域 (pLDDT>70) | 仅零星短片段 (650-669: 20aa, pLDDT=85.2) |
| PAE 矩阵尺寸 | 1259×1259 |
| PAE 均值 | 28.42 |
| PAE <5 Å 占比 | 0.5% |
| PAE <10 Å 占比 | 1.1% |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/AUTS2/AUTS2-PAE.png]]

**评价**: AUTS2 几乎完全无序，88.6%的残基 pLDDT < 50。仅 650-669 区域有一小段高置信度折叠（20 aa, pLDDT 85.2）。PAE 图显示几乎没有任何域结构信号。这是一个典型的内在无序蛋白 (IDP)，可能在结合伙伴后才获得折叠。不适合传统的结构生物学研究。得分 2/10。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | AUTS2 family (IPR023246) |
| UniProt | 无经典结构域注释; 仅标注多个 disordered regions (1-87, 108-285, 299-470, 771-1027, 1119-1146) |

**染色质调控潜力分析**:
AUTS2 是一个经典的内在无序蛋白 (IDP)。UniProt 标注了 5 段大范围无序区域。InterPro 仅注释了 AUTS2 家族域，无任何 DNA 结合或染色质修饰结构域。虽然 AUTS2 在功能上参与 PRC1 介导的 H2A 泛素化调控，但其本身缺乏直接催化或识别染色质修饰的结构域——它的角色更像是支架蛋白或调控亚基。

**得分 3/10**: 无经典染色质结构域，蛋白已被 >200 篇论文研究仍无注释结构域。内在无序性是其本质特征而非批评，但限制了作为独立酶学单位的可操作性。

#### 3.6 PPI :
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| CSNK2B | 0.999 | CK2 激酶调节亚基 | ⚠️ 间接 |
| CSNK2A2 | 0.993 | CK2 激酶催化亚基 | ⚠️ 间接 |
| PCGF5 | 0.922 | PRC1 核心组分, H2A泛素连接酶 | ✅ 染色质修饰 |
| RNF2 | 0.911 | PRC1 核心 E3 连接酶 (RING1B) | ✅ 染色质修饰 |
| RYBP | 0.899 | PRC1 组分, 促进 H2Aub | ✅ 染色质修饰 |
| YAF2 | 0.893 | PRC1 相关转录调控 | ✅ 转录调控 |
| BMI1 | 0.876 | PRC1 核心组分 | ✅ 染色质修饰 |
| RING1 | 0.819 | PRC1 核心 E3 连接酶 (RING1A) | ✅ 染色质修饰 |
| PCGF3 | 0.783 | PRC1 组分 | ✅ 染色质修饰 |
| CBX2 | 0.649 | PRC1 染色质阅读器 (chromodomain) | ✅ 染色质阅读 |
| DCAF7 | 0.607 | DDB1-CUL4 泛素连接酶 | ⚠️ 间接 |
| PHC1 | 0.589 | PRC1 组分 | ✅ 染色质修饰 |
| SCMH1 | 0.500 | PRC1 相关 Polycomb 蛋白 | ✅ 染色质修饰 |
| EP300 | 0.470 | 组蛋白乙酰转移酶 (p300) | ✅ 染色质修饰 |

**UniProt 实验验证互作**:
- EP300 (6 experiments)
- PCGF5 (8 experiments)
- RNF2 (7 experiments)

**PPI 互证**:
- humanPPI 数据缺失，基于 STRING + UniProt 互作数据
- 两个独立来源 (STRING genomics + UniProt IntAct) 均确认 PCGF5、RNF2、EP300

**调控相关比例**: 11/14 unique partners (78.6%)

**评价**: AUTS2 的 PPI 、BMI1、RING1A 等核心组分。EP300 (p300 HAT) 提供组蛋白乙酰化连接。UniProt 实验证实 PCGF5、RNF2、EP300 直接互作。CK2 激酶 (CSNK2B/A2) 通过磷酸化 RNF2 调节其泛素连接酶活性。/ PDB | 无PDB实验结构; 预测几乎完全无序 | N/A |

| 结构域 | InterPro / UniProt | 仅AUTS2家族域; 无多源交叉验证 | 一致但贫乏 |
|---|---|---|---|
| 定位 | Protein Atlas / UniProt / GO | 一致确认核定位 (含额外胞质定位) | ⚠️ 部分一致 |
| 进化保守 | 人类-小鼠 | 小鼠 Auts2 明确同源物 | ✅ 保守 |

**互证加分明细**:
- 定位互证：Protein Atlas (supported) + UniProt (Nucleus, PubMed evidence) → ≥2源 → **+0.5**
- 进化保守性：小鼠 Auts2 同源物 → **+0.5**
- 结构域互证：仅 InterPro 检出 AUTS2 家族域, 未达 ≥3 源标准 → **0**
- PPI 互证：humanPPI 不可访问 → **0**
- 三维结构互证：无 PDB 实验结构 → **0**

**总分**: +1.0 / max +3

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 见 3.4 节 | — |
| 结构域 | UniProt / InterPro / Pfam | 见 3.5 节 | — |
| PPI | STRING | 见 3.6 节 | — |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus | ✅ |

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. **PRC1 染色质连接**: 实验验证与 PRC1 核心组分 (PCGF5/RNF2) 和 EP300 直接互作, 染色质调控背景明确。
2. **疾病关联**: AUTS2 相关综合征 (智力障碍/自闭症) 提供明确的疾病生物学背景。
3. **PRC1-chromatin niche**: 在 AUTS2 的 220 篇论文中, 染色质/PRC1 方向占比 <20%, 仍有 niche 空间。

**风险/不确定性**:
1. **内在无序蛋白**: 88.6% 残基无序, 不适合传统结构生物学和酶学分析。需要合作蛋白共表达或固有无序蛋白 (IDP) 专用方法。
2. **双重定位**: 核质+胞质双重分布, 功能混杂。核内功能与胞质 (神经元) 功能难以分离。
3. **大蛋白**: 1259 aa 不利于全长重组表达和生化实验。可能需要截短体策略, 但截短体的功能验证困难。
4. **支架蛋白角色**: 作为 PRC1 调控亚基而非催化亚基, 缺乏独立的酶学活性。研究可能需要整个 PRC1 亚复合体重组。

**下一步建议**:
- [ ] 构建 AUTS2 N端/C端或保守区域截短体进行功能定位
- [ ] Co-IP 验证内源 PCGF5/RNF2/EP300 互作
- [ ] AUTS2 KD 后检测 H2Aub 水平和 PRC1 靶基因表达变化
- [ ] 考虑用 IDP 专用方法 (NMR, SAXS, smFRET) 研究构象动态

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXX7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158321-AUTS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AUTS2%5BTitle/Abstract%5D (220 results)
- STRING: https://string-db.org/ (AUTS2, 179 total partners)
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q8WXX7/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXX7
- - SMART: ⚠️ 未成功获取 (使用 UniProt+InterPro 结构域数据替代)
- humanPPI: ⚠️ 未成功获取 (使用 STRING+UniProt 互作数据替代)

![[Projects/TEreg-finding/protein-interested/detail/rejected/AUTS2/AUTS2-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/AUTS2/AUTS2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WXX7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR023246; |
| Pfam | PF15336; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158321-AUTS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2B | Biogrid, Opencell | true |
| EP300 | Intact, Biogrid | true |
| PCGF5 | Intact, Biogrid | true |
| RNF2 | Intact, Biogrid | true |
| CSNK2A1 | Biogrid | false |
| CSNK2A2 | Biogrid | false |
| DCAF7 | Biogrid | false |
| PCGF3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
