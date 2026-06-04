---
type: protein-evaluation
gene: "ADNP"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ADNP 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ADNP / ADNP1, KIAA0784 |
| 蛋白大小 | 1102 aa / 123.6 kDa |
| UniProt ID | Q9H2P0 |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 10 | ×3 | 30.0 | UniProt: Nucleus + Chromosome, 染色质结合蛋白 |
| 📏 蛋白大小 | 8 | ×2 | 16.0 | 1102 aa, 123.6 kDa, 800-1200 aa 范围 |
| 🆕 研究新颖性 | 5 | ×3 | 15.0 | 324 篇总发表, 90 篇 chromatin 方向, 神经发育为主 |
| 🏗️ 三维结构 | 4 | ×3 | 12.0 | pLDDT 56.2, 36.3% 有序, 54% 无序, PAE 均值 27.9 Å |
| 🧬 调控结构域 | 10 | ×2 | 20.0 | Homeodomain + C2H2 zinc fingers, ≥5来源一致确认 |
| 🔗 PPI | 4/10 | ×3 | **12** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | — | max +3 | 1.5 | 结构域≥3来源 +0.5; 域功能一致 +0.5; 定位多源一致 +0.5 |
| **原始总分** | | | **119.5**/158 | |
| **归一化总分** | | | **75.6**/100 | |

### 3. 详细分析

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/ADNP/IF_images/A431_HPA006371_1.jpg|A431_HPA006371_1]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/ADNP/IF_images/U2OS_HPA050560_1.jpg|U2OS_HPA050560_1]]

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus; Chromosome | Swiss-Prot reviewed, ECO 证据 |
| GeneCards | Nucleus (predicted) | 计算预测 |

**结论**: UniProt 明确标注 Nucleus + Chromosome。ADNP 被注释为染色质结合蛋白，具有 homeobox DNA-binding domain，该域通常介导核定位和 DNA 结合。得分 10。

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 1102 aa, 123.6 kDa，处于 800-1200 aa 范围。大小偏大但仍适合常规生化实验 (可纯化表达)。大尺寸可能带来表达纯化难度稍高但可接受。得分 8。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 (含 ADNP1) | 324 |
| 最早发表年份 | ~2001 |
| Chromatin/epigenetics 比例 | 90/324 (27.8%) |

**主要研究方向**:
- 神经发育与保护 (ADNP 综合征/ Helsmoortel-Van der Aa 综合征, 自闭症谱系障碍)
- 染色质重塑 (SWI/SNF 复合体互作, HP1 结合)
- 转录调控 (homeobox 转录因子功能)
- 细胞骨架/自噬 (MAP1LC3B 互作)

**评价**: 324 篇发表，处于 200-500 范围。chromatin/epigenetics 方向占比约 28%, 属于成熟子领域而非全新方向。得分 5 (不加分)。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 56.2 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 36.3% (400/1102) |
| pLDDT > 90 占比 | 5.4% (60/1102) |
| pLDDT 70-90 占比 | 30.9% (340/1102) |
| pLDDT < 50 占比 | 54.0% (595/1102) |
| PAE 矩阵尺寸 | 1102 × 1102 |
| PAE 总体均值 | 27.9 Å |
| PAE < 5 Å 占比 | 1.6% |
| PAE < 10 Å 占比 | 3.0% |

**pLDDT 解析**:
- 超过半数残基 (54%) pLDDT < 50, 为高度无序区域
- 仅 60 个残基 (5.4%) pLDDT > 90, 高置信度折叠极少
- 有序区域分散为 17 个小片段 (最长仅 92 aa), 无大型连续折叠域
- 主要有序块: 72-130 (59 aa, 可能对应 homeodomain 附近), 445-536 (92 aa), 751-820 (70 aa)

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/ADNP/ADNP-PAE.png]]

**PAE 数值分析**:
- PAE 均值 27.9 Å, 整体预测误差极大
- PAE < 5 Å 仅占 1.6%, 几乎无可辨识的刚性折叠域间接触
- PAE < 10 Å 仅占 3.0%, 域间组织高度松散
- 对角线 PAE < 5 为 100% (连续链内接触正常)

**评价**: 结构预测质量偏低。pLDDT 均值仅 56.2, 54% 残基无序。PAE 图整体模糊, 缺乏清晰域间低 PAE 块, 提示 ADNP 为高度固有无序蛋白 (IDP), 可能在结合 partner 后才折叠。这与许多染色质调控蛋白 (如转录因子) 的特征一致 —— 固有无序区域介导多价互作。得分 4。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| UniProt/InterPro | ADNP/ADNP2 family (IPR045133), ADNP_Znf (IPR045134), Homeodomain (IPR009057), C2H2 Znf (IPR013087) |
| Pfam | ADNP_N (PF16615), Homeodomain (PF00046) |
| SMART | HOX (SM00389), ZnF_C2H2 (SM00355) |
| PROSITE | HOMEOBOX_2 (PS50071), ZINC_FINGER_C2H2_1 (PS00028), ZINC_FINGER_C2H2_2 (PS50157) |

**染色质调控潜力分析**:
- **Homeodomain**: 经典 DNA 结合域, 识别特定 DNA 序列并调控转录。homeodomain 蛋白是发育和细胞命运决定的核心转录因子
- **C2H2 zinc fingers (×8)**: 经典 DNA 结合模块, 由 PROSITE 和 SMART 双重确认。C2H2 ZF 是最常见的 DNA 结合域类型, 广泛存在于染色质调控蛋白中
- **ADNP_N domain**: ADNP 家族 N 端保守域, 功能可能与蛋白互作或染色质靶向有关
- ≥5 个独立数据库 (UniProt, InterPro, Pfam, SMART, PROSITE) 一致确认 homeodomain 和锌指结构域
- GO 注释和 UniProt 功能描述均指向 DNA 结合和转录调控

**评价**: 域结构完美符合染色质/DNA 调控蛋白特征。Homeodomain + 8×C2H2 zinc fingers 的组合是转录因子的经典域架构。得分 10。

#### 3.6 PPI — 前 30 partners:
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| CHD4 | 0.991 | NuRD 复合体染色质重塑 ATPase | 是 |
| CBX3 | 0.856 | HP1γ, H3K9me3 reader | 是 |
| CBX1 | 0.848 | HP1β, H3K9me3 reader | 是 |
| CHD8 | 0.835 | CHD 家族染色质重塑 | 是 |
| CBX5 | 0.819 | HP1α, H3K9me3 reader | 是 |
| ZBTB14 | 0.778 | 锌指转录因子 | 是 |
| ARID1A | 0.754 | SWI/SNF (BAF) 亚基 | 是 |
| BPTF | 0.741 | NURF 复合体, 核小体重塑因子 | 是 |
| SMARCC2 | 0.741 | SWI/SNF (BAF) 核心亚基 | 是 |
| POGZ | 0.716 | 锌指蛋白, 异染色质调控 | 是 |
| GLRX | 0.713 | 谷氧还蛋白 | 否 |
| KMT5B | 0.713 | H4K20 甲基转移酶 | 是 |
| DYRK1A | 0.648 | 激酶 | 否 |
| SMARCA4 | 0.640 | SWI/SNF (BAF) ATPase BRG1 | 是 |
| TRIP12 | 0.633 | E3 泛素连接酶 | 否 |
| ASH1L | 0.631 | H3K36 甲基转移酶 | 是 |
| ZNF597 | 0.608 | 锌指蛋白 | 是 |
| ARID1B | 0.595 | SWI/SNF (BAF) 亚基 | 是 |
| SMARCA5 | 0.584 | ISWI 染色质重塑 ATPase | 是 |
| ZC3H4 | 0.583 | 锌指蛋白, RNA 结合 | 是 |
| BRD4 | 0.571 | BET 家族, 乙酰化 reader | 是 |
| MED13L | 0.568 | Mediator 复合体亚基 | 是 |
| DPM1 | 0.565 | 代谢酶 | 否 |
| MAP1LC3B | 0.549 | 自噬相关 | 否 |
| MAPRE3 | 0.548 | 微管结合 | 否 |
| NCKAP1 | 0.543 | 细胞骨架调控 | 否 |
| ZNF292 | 0.540 | 锌指转录因子 | 是 |
| KDM2A | 0.540 | H3K36 去甲基化酶 | 是 |
| KDM1A | 0.536 | H3K4me1/2 去甲基化酶 (LSD1) | 是 |
| CHAMP1 | 0.534 | 染色体排列维护 | 是 |

**调控相关分类统计**:
- 染色质重塑: 6 (CHD4, CHD8, BPTF, SMARCA4, SMARCA5, SMARCC2)
- SWI/SNF 亚基: 3 (ARID1A, ARID1B, SMARCC2)
- HP1/异染色质 reader: 3 (CBX1, CBX3, CBX5)
- 组蛋白修饰酶 (writer/eraser): 4 (KMT5B, ASH1L, KDM2A, KDM1A)
- 乙酰化 reader: 1 (BRD4)
- Mediator/转录共调控: 1 (MED13L)
- 锌指转录因子: 4 (ZBTB14, POGZ, ZNF597, ZNF292, ZC3H4)
- 染色体结构: 1 (CHAMP1)
- **调控相关合计**: 23/30 (76.7%)

**humanPPI**: **PPI 互证**: 仅有 STRING 数据, 无 humanPPI 对比。但 STRING , 组蛋白修饰 (KMT5B, ASH1L, KDM1A/LSD1, KDM2A), 异染色质 (HP1α/β/γ), 和 BET reader (BRD4)。这是典型的染色质调控中枢蛋白的 PPI 特征。得分 10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold pLDDT 56.2 | 高度无序蛋白, 无实验 PDB | — |
| 结构域 | UniProt / InterPro / Pfam / SMART / PROSITE | ≥5 来源一致: Homeodomain + C2H2 ZF | 是 |
| PPI | STRING | 76.7% 调控相关, 多复合体交叉验证 | — (仅 STRING) |
| 定位 | UniProt: Nucleus + Chromosome | 染色质结合蛋白 | 内部一致 |

**互证加分明细**:
- 结构域 ≥3 个独立来源一致检出 Homeodomain + C2H2 ZF: **+0.5**
- 域的功能注释 (GO/UniProt) 与染色质调控一致: **+0.5**
- UniProt 多条注释一致确认 Nucleus + Chromosome 定位: **+0.5**
- **总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 明确的染色质调控蛋白: Homeodomain + 8×C2H2 ZF, 经典转录因子结构域架构, 5+ 数据库交叉验证
2. 顶级的染色质 PPI , SWI/SNF (ARID1A/B, SMARCA4, SMARCC2), ISWI (SMARCA5), HP1 (CBX1/3/5), 组蛋白修饰酶 (LSD1/KDM1A, KMT5B, ASH1L), BRD4 等染色质核心因子高度互作
3. 核定位明确: Nucleus + Chromosome
4. 生物学重要性高: ADNP 突变导致严重神经发育综合征, 染色质功能有转化医学价值

**风险/不确定性**:
1. 三维结构质量差: 54% 无序, 仅 36% 有序区域, pLDDT 均值 56.2。高度固有无序特征使结构解析极具挑战
2. 大蛋白 (1102 aa) 表达纯化难度较高
3. 研究已有 324 篇, 新颖性中等; chromatin 方向相对成熟 (28% 发表)
4. 固有无序区域的具体功能和折叠机制未明, 研究需要 partner 共表达或截短体策略

**下一步建议**:
- [ ] 重点研究 homeodomain 或锌指域截短体的 DNA 结合特异性和结构
- [ ] 利用 ChIP-seq/CUT&RUN 确定 ADNP 全基因组结合谱
- [ ] 通过 co-IP/MS 验证与 SWI/SNF 和 NuRD 复合体的内源互作
- [ ] 有序区域 (72-130, 445-536, 751-820) 可作为结构解析的切入点

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H2P0
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2P0
- STRING: https://string-db.org/network/9606.ENSP00000360662
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ADNP
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q9H2P0/

![[Projects/TEreg-finding/protein-interested/detail/rejected/ADNP/ADNP-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ADNP/ADNP-PAE.png]]




